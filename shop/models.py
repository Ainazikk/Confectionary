from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, blank=False, verbose_name='имя')
    slug = models.SlugField(max_length=200, blank=True, null=True, verbose_name='родительская категория')


    def __str__(self):
        return f"{self.name}{self.slug}"
        

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        db_table = 'Category'



class Products(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    quantity = models.IntegerField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='product_images', blank=True)

    
    def __str__(self):
        return f"{self.name}{self.slug}{self.category}{self.price}{self.description}{self.quantity}{self.created_date}{self.image}"
        

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        db_table = 'Products'
