from django.urls import path
from .views import services

app_name = "services_page"

urlpatterns = [
    path("", services, name="services"),
]
