from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from shop.models import Products
from .cart import Cart
from .forms import CartAddProductForm



def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    return render(request, 'cart_detail.html', {'cart': cart})



def cart_add_from_main(request, product_id):
    cart = Cart(request)    
    product = get_object_or_404(Products, id=product_id)    
    cart.add(product)
    return redirect('cart:cart_detail')



@require_POST
def cart_add_product(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_delete_product(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')



