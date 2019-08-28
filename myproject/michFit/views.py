from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .forms import CartAddProductForm
from django.http import HttpResponse, Http404
from .models import MenuItem
from . import calorieCounter
cart = []

def home(request):
    menu = MenuItem.objects.order_by('-name')[:]
    context = {'menu': menu}
    MenuItem.objects.all().delete()
    for key, value in calorieCounter.itemsDict.items():
        MenuItem.objects.create_item(key, value[0],value[1])
    return render(request,'michFit/index.html',context)

def detail(request,name):
    try:
        item=MenuItem.objects.get(pk=name)
    except MenuItem.DoesNotExist:
        raise Http404("Item does not exist")
    return render(request, 'michFit/detail.html',{'item': item})

def addCart(request,item_id):
    cart.append(item_id)
def viewCart(request):
    return render(request,'michFit/cart.html')
    
