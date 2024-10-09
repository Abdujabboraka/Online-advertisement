from django.db import models
from address.models import AddressField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='category-image/', null=True, blank=True)

    def __str__(self):
        return self.name

class Ad(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=250, null=True, blank=True,default='no description')
    image = models.ImageField(upload_to='ads', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = AddressField(on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

