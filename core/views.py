from django.shortcuts import render
from views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'
