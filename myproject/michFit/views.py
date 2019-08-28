from django.shortcuts import render


from django.http import HttpResponse, Http404
from .models import MenuItem
from . import calorieCounter
cart = []
totalCalories = 0
totalProtein = 0
def home(request):
    menu = MenuItem.objects.order_by('name')[:]
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

def cartdelete(request, item_id):
    cart.remove(MenuItem.objects.get(pk=item_id))
    totalCalories = 0
    totalProtein=0
    for item in cart:
        totalCalories += item.calories
        totalProtein+=item.protein
    return render(request,'michFit/cart.html',{'cart': cart, 'totalCalories': totalCalories, 'totalProtein': totalProtein} )

def cart_add(request, item_id):
    cart.append(MenuItem.objects.get(pk=item_id))
    totalCalories = 0
    totalProtein=0
    for item in cart:
        totalCalories += item.calories
        totalProtein+=item.protein
    
    return render(request, 'michFit/cart.html',{'cart': cart, 'totalCalories': totalCalories, 'totalProtein': totalProtein} )
    
def cart_view(request):
    totalCalories = 0
    totalProtein=0
    for item in cart:
        totalCalories += item.calories
        totalProtein+=item.protein
    return render(request, 'michFit/cart.html',{'cart': cart, 'totalCalories': totalCalories, 'totalProtein': totalProtein} )