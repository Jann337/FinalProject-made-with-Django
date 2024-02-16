from django.urls import path
from . import views

app_name = 'account_page'

urlpatterns = [
    path("register/", views.register_customer, name="register"),
    path("login/", views.login_customer, name="login"),
    path("logout/", views.logout_customer, name="logout")
]
