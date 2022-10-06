from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *

 
def store(request):
    category = ''
    if request.method == 'POST':
        category = request.POST['category']
        if category=='all':
            products = Product.objects.all()
        else:
            products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()
    context = {
        'products': products,
        'category': category
    }
    return render(request, 'store/store.html', context)

def cart(request):
    if request.user.is_authenticated():
        customer = request.user.customer
    context ={}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context ={}
    return render(request, 'store/checkout.html', context)

