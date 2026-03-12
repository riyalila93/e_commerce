from django.urls import path

from . import views


app_name = "products"

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    path("product/<int:pk>/add-to-cart/", views.add_to_cart, name="add_to_cart"),
    path("product/<int:pk>/like/", views.like_product, name="like_product"),
    path("cart/", views.cart_view, name="cart"),
    path("wishlist/", views.wishlist_view, name="wishlist"),
]
