from django.urls import path
from . import views

app_name = "backoffice_home"

urlpatterns = [
    path("",  views.back_office_home, name="home"),
]
