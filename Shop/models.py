from django.db import models
from Client.models import customer
# Create your models here.

class AddProduct(models.Model):
    Product_name = models.CharField(max_length=100)
    Catagory = models.CharField(max_length=200)
    cost = models.FloatField(max_length=200)
    image = models.ImageField(upload_to='products/images/',null=True, blank=True)


    def __str__(self):
        return self.Product_name

class OrderProduct(models.Model):
    product = models.ForeignKey(AddProduct, on_delete=models.CASCADE)
    quantity = models.IntegerField(max_length=20, null=True, blank=True)
    customer_Id = models.ForeignKey(customer, on_delete=models.CASCADE)

    PAYMENT_CHOICES = (
        ('Bkash', 'Bkash'),
        ('Rocket', 'Rocket'),
        ('Cash On Delivery', 'Cash On Delivery')
    )
    payment = models.CharField(max_length=30, choices=PAYMENT_CHOICES, default='Cash On Delivery')

    transaction_id = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.customer_Id.name + ", " + self.customer_Id.address + ", " + self.customer_Id.contact + " : " + self.product.Product_name + "(" + self.payment + ")"