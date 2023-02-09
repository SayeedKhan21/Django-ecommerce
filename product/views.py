from django.shortcuts import render
from django.views import generic
from .models import (
    Product ,
    Cart ,
    CartItems ,
)


# Create your views here.


class ProductDetailView(generic.DetailView) :  
    queryset = Product.objects.all()
    context_object_name = 'product'
    template_name = 'products/product_detail.html'

    def get_context_data(self, **kwargs) :

        """ Modifying price based on size of product  """
        product = self.get_object()
        size_name = self.request.GET.get('size')
        price = 0
        price = product.get_product_correct_price(size_name)
        context =  super().get_context_data(**kwargs)
        context['new_price'] = price
        context['selected_size'] = size_name
        return context
        

       
    



