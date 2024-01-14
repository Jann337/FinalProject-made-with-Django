from django.shortcuts import render, redirect
from .models import Variables
from django.http import HttpResponseBadRequest


def settings(request):
    variables, created = Variables.objects.get_or_create(
        pk=1)

    if created:

        variables.website_title = "Default Title"

        variables.save()

    if request.method == 'POST':
        website_title = request.POST.get("title")
        description = request.POST.get("description")
        currency = request.POST.get("currency")

        if website_title:
            variables.website_title = website_title
        if description:
            variables.homepage_description = description
        if currency:
            variables.website_currency = currency

        try:
            variables.save()
        except Exception as e:
            return HttpResponseBadRequest("Error: " + str(e))

    return render(request, "settings.html", {'variables': variables})
