from django.shortcuts import render, get_object_or_404
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required


@login_required(login_url='supplier:login')
def order_list(request):
    orders = Order.objects.all()

    return render(request, "orders.html", {"orders": orders})


@login_required(login_url='supplier:login')
def order_detail(request, order_number):
    order = get_object_or_404(
        Order, order_number=order_number)
    products_in_order = order.order_products.all()
    order_items = OrderItem.objects.filter(order=order)

    return render(request, "order_detail.html", {"order": order, "products_in_order": products_in_order, "order_items": order_items})
