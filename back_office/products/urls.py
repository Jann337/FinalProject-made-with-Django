from django.urls import path
from .views import products, product_detail

app_name = "backoffice_products"

urlpatterns = [
    path('', products, name='products'),
    path('<int:product_id>/', product_detail, name='product_detail')
]
