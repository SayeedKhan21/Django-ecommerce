from django.shortcuts import render
from django.views import generic
from product.models import (
    Product ,
)
# Create your views here.

class IndexView(generic.ListView) : 

    model = Product
    context_object_name = 'products'
    template_name = 'home/index.html'

