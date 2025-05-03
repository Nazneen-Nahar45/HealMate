from django.contrib import admin
from .models import Product_Bill
from .models import Service_Bill

# Register your models here.
admin.site.register(Product_Bill)
admin.site.register(Service_Bill)