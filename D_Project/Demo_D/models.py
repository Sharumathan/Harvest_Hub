from django.db import models

# Create your models here.

class Billing_Address(models.Model):
    Name = models.CharField(max_length=100 , default='')
    Email = models.CharField(max_length=100 , default='')
    Address = models.CharField(max_length=100, default='')
    State = models.CharField(max_length=100 , default='')
    Zip = models.IntegerField(default='')


class Order(models.Model):
    pass