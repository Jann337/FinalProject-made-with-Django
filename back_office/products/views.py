from django.shortcuts import render
from .forms import ProductForm

def add(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            # Process the form data
            return HttpResponseRedirect('/success/')  # Redirect after POST
    else:
        form = ProductForm()
    return render(request, 'backoffice_products.html', {'form': form})
