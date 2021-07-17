from django.shortcuts import render, get_object_or_404
from .models import Category, Products
from django.core.paginator import Paginator
from django.views.generic import ListView
from cart.forms import CartAddProductForm


def index(request):
    categories=Category.objects.all()
    return render(request, 'index.html', {'categories': categories})



def product_list(request, category_slug=None): 
     
    category = None
    categories = Category.objects.order_by('-id')
    products = Products.objects.all()
    

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    paginator = Paginator(products, 2)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(request,'products.html',
        {'category': category,
        'categories': categories,
        'products': products})
        


def product_detail(request, product_id):
    product= get_object_or_404(Products, id=product_id)  
    cart_product_form = CartAddProductForm()  
    return render(request, 'product_detail.html', {'product': product, 'cart_product_form': cart_product_form})


def category_list(request):
    categories=Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def about_us(request):
    return render(request, 'about_us.html')


class ProductList(ListView):
    model = Products


def products(request):
    return render(request, 'products.html')


def blog_details(request,id):
    product = Products.objects.get(id = id)
    return render(request, 'blog/blog_details.html', {'blog': blog})


def checkout(request):
    return render(request, 'checkout.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')
