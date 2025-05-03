from django.db import models
from Client.models import customer
from Shop.models import AddProduct
from Service.models import Service

# Create your models here.
class Product_Bill(models.Model):
    bill_no = models.IntegerField()
    amount = models.IntegerField()
    type = models.CharField(max_length=100)
    p_id = models.ForeignKey(AddProduct,on_delete=models.CASCADE)
    c_id = models.ForeignKey(customer,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.bill_no)

class Service_Bill(models.Model):
    bill_no = models.IntegerField()
    amount = models.IntegerField()
    type = models.CharField(max_length=100)
    s_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    c_id = models.ForeignKey(customer,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.bill_no)