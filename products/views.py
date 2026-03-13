
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST

from .forms import LoginForm, SignupForm
from .models import CartItem, Category, Product, WishlistItem


def product_list(request):
    category_name = request.GET.get("category")
    categories = Category.objects.all()
    preferred_order = ["Women", "Men", "Kids", "Shoes", "Accessories"]
    ordered_categories = sorted(
        categories,
        key=lambda category: (
            preferred_order.index(category.name)
            if category.name in preferred_order
            else len(preferred_order),
            category.name,
        ),
    )

    products = Product.objects.select_related("category").order_by("name")
    query = request.GET.get("q")
    if query:
        products = products.filter(Q(name__icontains=query) | Q(brand__icontains=query))

    active_category = None
    if category_name:
        active_category = next(
            (category for category in ordered_categories if category.name == category_name),
            None,
        )
        if active_category:
            products = products.filter(category=active_category)

    cart_product_ids = set()
    wishlist_product_ids = set()
    if request.user.is_authenticated:
        cart_product_ids = set(
            CartItem.objects.filter(user=request.user).values_list("product_id", flat=True)
        )
        wishlist_product_ids = set(
            WishlistItem.objects.filter(user=request.user).values_list("product_id", flat=True)
        )

    return render(
        request,
        "products/product_list.html",
        {
            "products": products,
            "categories": ordered_categories,
            "active_category": active_category,
            "cart_product_ids": cart_product_ids,
            "wishlist_product_ids": wishlist_product_ids,
        },
    )


def product_detail(request, pk):
    product = get_object_or_404(
        Product.objects.select_related("category"),
        pk=pk,
    )
    next_url = request.GET.get("next") or reverse("products:product_list")
    return render(
        request,
        "products/product_detail.html",
        {
            "product": product,
            "next_url": next_url,
        },
    )


def login_view(request):
    if request.user.is_authenticated:
        return redirect("products:product_list")

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("products:product_list")
    else:
        form = LoginForm(request)

    return render(request, "auth/login.html", {"form": form})


def signup_view(request):
    if request.user.is_authenticated:
        return redirect("products:product_list")

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("products:product_list")
    else:
        form = SignupForm()

    return render(request, "auth/signup.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("products:product_list")


def dashboard_view(request):
    return redirect("products:product_list")


@require_POST
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if not request.user.is_authenticated:
        messages.info(request, f"Please log in to add {product.name} to your cart.")
        return redirect("login")

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={"quantity": 1},
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save(update_fields=["quantity"])
    messages.success(request, f"{product.name} added to cart.")
    return redirect(request.META.get("HTTP_REFERER", "products:cart"))


@require_POST
@login_required
def remove_from_cart(request, pk):
    cart_item = get_object_or_404(CartItem, user=request.user, product_id=pk)
    product_name = cart_item.product.name
    cart_item.delete()
    messages.success(request, f"{product_name} removed from cart.")
    return redirect("products:cart")


@require_POST
@login_required
def update_cart_quantity(request, pk):
    action = request.POST.get("action")
    cart_item = get_object_or_404(CartItem, user=request.user, product_id=pk)

    if action == "increase":
        cart_item.quantity += 1
    elif action == "decrease":
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
        else:
            cart_item.delete()
            return JsonResponse({"status": "removed"})

    cart_item.save()
    
    # Calculate totals for dynamic update
    item_total = cart_item.product.price * cart_item.quantity
    cart_items = CartItem.objects.filter(user=request.user)
    cart_total = sum(item.product.price * item.quantity for item in cart_items)
    
    return JsonResponse({
        "status": "updated",
        "quantity": cart_item.quantity,
        "item_total": float(item_total),
        "cart_total": float(cart_total)
    })


@require_POST
def like_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if not request.user.is_authenticated:
        messages.info(request, f"Please log in to like {product.name}.")
        return redirect("login")

    wishlist_item, created = WishlistItem.objects.get_or_create(
        user=request.user,
        product=product,
    )
    if created:
        messages.success(request, f"Added {product.name} to wishlist.")
    else:
        wishlist_item.delete()
        messages.success(request, f"Removed {product.name} from wishlist.")
    
    return redirect(request.META.get("HTTP_REFERER", "products:product_list"))


@require_POST
@login_required
def remove_from_wishlist(request, pk):
    wishlist_item = get_object_or_404(WishlistItem, user=request.user, product_id=pk)
    product_name = wishlist_item.product.name
    wishlist_item.delete()
    messages.success(request, f"{product_name} removed from wishlist.")
    return redirect("products:wishlist")


@login_required
def cart_view(request):
    cart_items = (
        CartItem.objects.filter(user=request.user)
        .select_related("product")
        .order_by("-created_at")
    )
    cart_rows = []
    cart_total = 0
    for item in cart_items:
        item_total = item.product.price * item.quantity
        cart_rows.append({"item": item, "item_total": item_total})
        cart_total += item_total

    return render(
        request,
        "products/cart.html",
        {
            "cart_rows": cart_rows,
            "cart_total": cart_total,
        },
    )


@login_required
def wishlist_view(request):
    wishlist_items = (
        WishlistItem.objects.filter(user=request.user)
        .select_related("product")
        .order_by("-created_at")
    )
    return render(
        request,
        "products/wishlist.html",
        {"wishlist_items": wishlist_items},
    )
