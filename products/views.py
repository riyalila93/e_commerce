
from django.shortcuts import get_object_or_404, render

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
