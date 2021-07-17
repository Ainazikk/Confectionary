from django.db import models
from django.contrib.auth.models import User
from shop.models import Products


class Customer(models.Model):
    customer_id = models.BigIntegerField(primary_key=True, editable=False)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    emailID = models.EmailField(max_length=254)
    favourite_products =  models.CharField(max_length=100)
    address = models.CharField(blank=True, null=True, max_length=150)


    def __str__(self):
        return f"{self.customer_id}{self.name}{self.password}{self.emailID}{self.favourite_products}{self.address}"
        

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        db_table = 'Customer'


class Order(models.Model): # One-To-One 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=50)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    country = models.CharField(max_length=250)
    city = models.CharField(max_length=250)

    class Meta: 
        ordering = ('-created_at',)

    def __str__(self):
        return f"Order {self.id}"

    def get_total_cost(self):
        return sum(item[price] * item[quantity] for item in self.items)
            

class OrderItem(models.Model): #One-To-Many 
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Products, related_name="order_items", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Orderitem {self.id} - Order {self.order.id}"
    
    def get_cost(self):
        return self.price * self.quantity 





  

