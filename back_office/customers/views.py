from django.shortcuts import render, get_object_or_404
from . import models
from django.contrib.auth.decorators import login_required


@login_required(login_url='supplier:login')
def customers(request):
    customers = models.UserDetail.objects.all()
    return render(request, "customers.html", {"customers": customers})


@login_required(login_url='supplier:login')
def customer_detail(request, customer_id):
    customer = get_object_or_404(models.UserDetail, id=customer_id)
    # You can add more logic here if needed
    return render(request, "customer_detail.html", {"customer": customer})
