'''radicals URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
'''
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: HttpResponseRedirect('home/')),
    path('backoffice/', include('back_office.home.urls')),
    path('backoffice/customers/', include('back_office.customers.urls')),
    path('backoffice/invoices/', include('back_office.invoices.urls')),
    path('backoffice/orders/', include('back_office.orders.urls')),
    path('backoffice/products/', include('back_office.products.urls')),
    path('backoffice/sales/', include('back_office.sales.urls')),
    path('backoffice/settings/', include('back_office.settings.urls')),
    path('backoffice/supplier/', include('back_office.supplier.urls')),
    path('about/', include('front_office.about_page.urls')),
    path('account/', include('front_office.account_page.urls')),
    path('contacts/', include('front_office.contacts_page.urls')),
    path('home/', include('front_office.home_page.urls')),
    path('products/', include('front_office.products_page.urls')),
    path('services/', include('front_office.services_page.urls')),
    path('shoppingcart/', include('front_office.shopping_cart_page.urls')),
    path('checkout/', include('front_office.checkout_page.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
