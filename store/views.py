from django.shortcuts import render
from .models import *

def store(request):
     Products = Product.objects.all()
     context = {'products':Products}
     return render(request, 'store/store.html', context)

def cart(request):
     context = {}
     return render(request, 'store/cart.html', context)

def checkout(request):
      context = {}
      return render(request, 'store/checkout.html', context)
