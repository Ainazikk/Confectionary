from django.db import models
from django.contrib.auth.models import User
from shop.models import Products


    

class Customer(models.Model):
    customer_id = models.ForeignKey(User, unique=True)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    emailID = models.CharField(max_length=254)
    favourite_products =  models.CharField(max_length=100)
    address = models.CharField(blank=True, null=True)


  

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    country = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
   


   
            

class OrderItems(models.Model): 
    order_id = models.ForeignKey(Orders, related_name="items", on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, related_name="order_items", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    

