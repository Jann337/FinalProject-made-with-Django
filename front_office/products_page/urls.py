from django.urls import path
from . import views

app_name = "products_page"

urlpatterns = [
    path("", views.products_page, name="products"),
    path("product/<product_id>/", views.product_detail, name="product_detail"),
]
