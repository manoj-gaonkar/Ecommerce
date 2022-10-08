from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
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
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Orders.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = { 'get_cart_total':0 }
    context ={ 'items': items , 'order': order}
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Orders.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = { 'get_cart_total':0 }
    context ={ 'items': items , 'order': order}
    return render(request, 'store/checkout.html', context)

def updateItem(request):
    return JsonResponse('added to cart ')

