from django.shortcuts import render, get_object_or_404
from . import models
from django.contrib.auth.decorators import login_required


@login_required(login_url='supplier:login')
def invoices(request):
    invoices = models.InvoiceDetail.objects.all()
    return render(request, "invoices.html", {"invoices": invoices})


@login_required(login_url='supplier:login')
def invoice_detail(request, invoice_id):
    invoice = get_object_or_404(models.InvoiceDetail, id=invoice_id)
    # You can add more logic here if needed
    return render(request, "invoice_detail.html", {"invoice": invoice})
