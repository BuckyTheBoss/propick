from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)


class SaleItem(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    available = models.BooleanField(default=True)


class Cart(models.Model):
    items = models.ManyToManyField(SaleItem)
    completed = models.DateTimeField(null=True)
    started = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
