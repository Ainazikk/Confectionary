from django.contrib import admin
from .models import Customer, Order, OrderItem
# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'name', 'password', 'emailID', ]
    list_filter = 'customer_id', 'name', 'password', 'emailID', 'favourite_products', 'address'
    



class OrderItemInline(admin.TabularInline):
    model = OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'address', 'postal_code', 'paid', 'created_at', 'updated_at']
    list_filter = ['paid', 'created_at']
    inlines = [OrderItemInline]
