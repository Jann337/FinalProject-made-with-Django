from django.urls import path
from . import views


app_name = 'customers'

urlpatterns = [
    path('', views.customers, name='customers'),
    path('<int:customer_id>/',
         views.customer_detail, name='customer_detail'),
]
