from re import template
from django.shortcuts import render
from  .models  import Product
from django.views.generic.edit import CreateView
from  .forms  import  ProductForm
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView


class ProductCreateView(CreateView):
    model = Product
    template_name='create.html'
    fields="__all__"
    success_url='/'



class ProductListView(ListView):
    model = Product
    template_name="read.html" 

class ProductDeleteView(DeleteView):
    template_name="delete.html"
    model = Product
    success_url='/'

class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name='update.html'
    success_url='/'
    