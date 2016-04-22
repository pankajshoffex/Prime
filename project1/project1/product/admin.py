from django.contrib import admin

from .models import Buyer, Measurement, Product
# Register your models here.

admin.site.register(Buyer)
admin.site.register(Measurement)
admin.site.register(Product)



