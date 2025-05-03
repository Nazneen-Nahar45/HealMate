from django.db import models

class Service(models.Model):
    service_name = models.CharField(max_length=100)
    service_for = models.CharField(max_length=100)
    service_cost = models.CharField(max_length=10)

    def __str__(self):
        return self.service_name