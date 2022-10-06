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
        ('apparel','Apparel'),
        ('smartphones','Smartphones'),
        ('speakers','Speakers'),
    )
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False )
    category = models.CharField(default='all', choices=CATEGORY, max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
     
    def __str__(self):
        return self.name
    # if there is no image for a certain product it shows an error so to encounter that we use @property 

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

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
    order = models.ForeignKey(Orders, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    pincode = models.CharField(max_length=200, null=True)
    order_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.address
    

    