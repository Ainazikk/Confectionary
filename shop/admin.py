from django.contrib import admin
from .models import Category, Products
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'category', 'price']
    list_filter = ('name', 'category')
    prepopulated_fields = {'slug': ('name',)}
