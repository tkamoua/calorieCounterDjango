from django.urls import path

from . import views


app_name = 'michFit'
urlpatterns = [
    path('', views.home, name='home'),
    path('<name>/',views.detail,name='detail'),
    path('cart/<item_id>/',views.cart_add, name='cart'),
    path('cart/view/<item_id>/',views.cart_view, name='cartview'),
    path('cartdelete/<item_id>/',views.cartdelete, name='cartdelete')
]