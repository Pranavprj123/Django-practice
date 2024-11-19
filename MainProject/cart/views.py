from django.shortcuts import render,get_object_or_404,redirect
from product.models import Product
from .models import Cart
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def add_to_cart(request,id):
    user_obj = get_object_or_404(User,username=request.user)
    cart_obj = Cart.objects.filter(user = user_obj)
    product_obj = get_object_or_404(Product,id = id)
    for item in cart_obj:
        if item.product.id == product_obj.id:
            print('hello')
            item.quantity +=1
            item.save()
            return redirect(request.META.get('HTTP_REFERER'))
    Cart.objects.create(user = user_obj,product = product_obj,quantity = 1)
    return redirect(request.META.get('HTTP_REFERER'))



def remove_from_cart(request,id):
    user_obj = get_object_or_404(User,username=request.user)
    cart_obj = Cart.objects.filter(user = user_obj)
    #product_obj = get_object_or_404(Product,id = id)
    for item in cart_obj:
        if item.id == id:
            item.delete()
            return redirect(request.META.get('HTTP_REFERER'))
    messages.error(request,'There is no product to remove from cart')
    return redirect(request.META.get('HTTP_REFERER'))

def update_cart(request):
    user_obj = get_object_or_404(User,username=request.user)
    cart_obj = Cart.objects.filter(user = user_obj)
    product_obj = get_object_or_404(Product,id = id)
    for item in cart_obj:
        product_quantity = request.GET.get(item.product.id)
        if product_quantity:
            item.quantity = product_quantity
            item.save()
    return redirect(request.META.get('HTTP_REFERER'))
    