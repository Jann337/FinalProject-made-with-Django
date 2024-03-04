from django.urls import path
from . import views

app_name = "products_page"

urlpatterns = [
    path("", views.products_page, name="products"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
]
