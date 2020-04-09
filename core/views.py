from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from .models import Item


class HomePageView(ListView):
    model = Item
    template_name = 'home.html'
    
