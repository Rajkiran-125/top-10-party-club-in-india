from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class RegisterModel(models.Model):
    username = models.CharField(max_length=50,blank=True)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

class LoginModel(models.Model):
    username = models.CharField(max_length=50,blank=True)
    password = models.CharField(max_length=50)


class ProductModel(models.Model):
    clubs= models.CharField(max_length=100, null=False, blank=False)
    sales= models.IntegerField()

    def __str__(self):
        return f'{self.clubs} - {self.sales}'


class BookingModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField(max_length=50)
    person = models.IntegerField(max_length=50)
    msg = models.CharField(max_length=100)

    
    
