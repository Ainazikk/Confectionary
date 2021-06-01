from django.db import models

# Create your models here.
class Category0(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)


class Products(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    category = models.ForeignKey(Category0, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    quantity = models.IntegerField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='product_images', blank=True)

