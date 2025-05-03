from django.contrib import admin
from .models import AddProduct
from .models import OrderProduct
# Register your models here.
admin.site.register(AddProduct)
admin.site.register(OrderProduct)