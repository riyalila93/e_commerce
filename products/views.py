
from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import LoginForm, SignupForm
from .models import Product


def product_list(request):
    products = Product.objects.select_related("category").order_by("name")
    return render(
        request,
        "products/product_list.html",
        {"products": products},
    )


def product_detail(request, pk):
    product = get_object_or_404(
        Product.objects.select_related("category"),
        pk=pk,
    )
    return render(
        request,
        "products/product_detail.html",
        {"product": product},
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

    messages.success(request, f"{product.name} added to cart.")
    return redirect("products:product_list")


@require_POST
def like_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if not request.user.is_authenticated:
        messages.info(request, f"Please log in to like {product.name}.")
        return redirect("login")

    messages.success(request, f"You liked {product.name}.")
    return redirect("products:product_list")
