from django.db import models
from Service.models import Service
from Client.models import customer

# Create your models here.
class Order(models.Model):
    disease = models.CharField(max_length=20)

    service = models.ForeignKey(Service, on_delete=models.SET_DEFAULT, default=1)
    client = models.ForeignKey(customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.client.name + ", " + self.client.address + ", " + self.client.contact + " : " + self.service.service_name + " ( cost " + self.service.service_cost + " )"


