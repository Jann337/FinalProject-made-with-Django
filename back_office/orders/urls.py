from django.urls import path
from . import views

app_name = 'back_office_orders'

urlpatterns = [
    path('', views.order_list, name='orders'),
    path('<order_number>/',
         views.order_detail, name='order_detail'),
]
