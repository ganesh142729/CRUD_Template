from django.shortcuts import render

# Create your views here.
from app.models import *

from django.views.generic import ListView , TemplateView,DetailView,CreateView,UpdateView


class Home(TemplateView):
    template_name='app/home.html'


class SchoolList(ListView):
    model=school
    context_object_name= 'schools'


class Schooldetail(DetailView):
    model= school
    context_object_name='schoolobj'
    
class SchoolCreate(CreateView):
    model=school
    fields='__all__'


    