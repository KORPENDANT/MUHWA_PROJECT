from pyexpat import model
from django.shortcuts import render
from django.views.generic import ListView
from .models import *

# Create your views here.
class CoffeeListView(ListView):
    model = Coffee
    template_name = 'menu/coffee.html'
    context_object_name = 'coffee_list'
    
class BeverageListView(ListView):
    model = Beverage 
    template_name = 'menu/beverage.html'
    context_object_name = 'beverage_list'
     
class DesertListView(ListView):
    model = Desert
    template_name = 'menu/desert.html'
    context_object_name = 'desert_list'
    
class SeasonmenuListView(ListView):
    model = SeasonMenu
    template_name = 'menu/seasonmenu.html'
    context_object_name = 'seasonmenu_list'


