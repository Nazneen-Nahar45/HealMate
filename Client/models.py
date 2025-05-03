from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    contact =models.CharField(max_length=20)
    # about = models.TextField(null=True)

    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)



    def __str__(self):
        return self.name

