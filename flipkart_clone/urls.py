
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from products import views as product_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", product_views.login_view, name="login"),
    path("signup/", product_views.signup_view, name="signup"),
    path("logout/", product_views.logout_view, name="logout"),
    path("dashboard/", product_views.dashboard_view, name="dashboard"),
    path("", include("products.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
