from django.urls import path

from . import views


app_name = 'michFit'
urlpatterns = [
    path('', views.home, name='home'),
    path('<name>/',views.detail,name='detail'),
  
]