from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null= True, blank=True)
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY =(
        ('all','All'),
        ('laptopaccessories','Laptop & accessories'),
        ('electronics','electronics'),
    )
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False )
    # Image
     
    def __str__(self):
        return name

class Orders(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Orders, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)

    