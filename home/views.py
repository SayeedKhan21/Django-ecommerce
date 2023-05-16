from django.shortcuts import render
from django.views import generic
from product.models import (
    Product ,
    Cart,
)
from django.views import View
# Create your views here.

class IndexView(View) : 

    def get(self ,request) : 
        products = Product.objects.all()
        context = {'products' : products}
        if request.user.is_authenticated : 
            
            cart = Cart.objects.filter(user = request.user , is_paid = False).first()
            if cart is None : 
                items_count = 0 
            else  :
                items_count = cart.get_total_cart_items()
            context['items_count'] = items_count

        return render(request , 'home/index.html' , context)

    def post(self ,request) : 
        category = request.POST.get('search-value')
        products = Product.objects.filter(category__category_name__icontains=category)
        context = {'products' : products}
        return render(request ,'home/index.html' ,context)

