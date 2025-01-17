from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import NewSupplierForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from . models import SupplierDetail


def register(request):
    if request.method == "POST":
        form = NewSupplierForm(request.POST)
        if form.is_valid():
            user = form.save()
            SupplierDetail.objects.create(user=user).save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("backoffice_home:home")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewSupplierForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("backoffice_home:home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("main:homepage")
