from django.contrib import admin
from django.urls import path
from product import views

app_name= 'product'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('goods', views.goods, name='goods'),

]