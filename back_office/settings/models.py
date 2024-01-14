from django.db import models


# Create your models here.


class Variables(models.Model):
    website_title = models.CharField(max_length=20, null=True)
    homepage_description = models.CharField(
        max_length=255, null=True)
    website_currency = models.CharField(max_length=10, null=True)
