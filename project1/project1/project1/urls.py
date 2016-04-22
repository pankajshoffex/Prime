"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from product.views import (
                    InvoicePDFView, 
                    HomeView, 
                    login_user, 
                    logout_user, 
                    create_invoice,
                    InvoiceListView,
                    )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^create/$', create_invoice, name='buyer_create'),
    url(r'^list/$', InvoiceListView.as_view(), name='buyer_list'),
    url(r'^login/$', login_user, name='login_user'),
    url(r'^logout/$', logout_user, name='logout_user'),
    url(r'^invoice.pdf$', InvoicePDFView.as_view(), name="invoice"),
]
