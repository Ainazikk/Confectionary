from django.shortcuts import render, get_object_or_404
from .models import Category, Products
from django.core.paginator import Paginator

def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')


def about(request):
    return render(request, 'about.html')




def product_list(request, category_slug=None): 
     
    category = None
    categories = Category.objects.order_by('-id')[:5]
    products = Products.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    paginator = Paginator(products, 2)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(request,'shop/product_list.html',
        {'category': category,
        'categories': categories,
        'products': products})
        

# def product_details(request, id, slug):
#     product = get_object_or_404(Products, id=id, slug=slug, available=True)
#     return render(request, 'shop/product_details.html', {'product_details': product_details})





