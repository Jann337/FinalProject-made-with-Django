from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# @login_required(login_url='supplier:login')
def back_office_home(request):
    return render(request, "back_office_home_page.html")
