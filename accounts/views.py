from django.shortcuts import render ,redirect
from django.urls import reverse
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate ,login ,logout
from django.contrib.auth import get_user_model
from product.models import (
    Product ,
    Cart ,
    SizeVariant ,
    CartItems ,
    Coupon ,
)
from django.conf import settings
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

import razorpay

# Create your views here.


class LoginView(View) : 

    def get(self ,request) : 
        return render(request , 'accounts/login.html')

    def post(self, request) : 
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = get_user_model().objects.filter(username= email)
        if not user.exists() : 
            messages.warning(request ,'Account not found Please Sign in to continue')
            return redirect(reverse('accounts:register'))
        
        user = authenticate(username = email , password = password)

        if user : 
            login(request , user)
            print(reverse('accounts:home'))
            return redirect(reverse('home:index'))
        
        messages.warning(request ,'Invalid credentials')
        return render(request , 'accounts/login.html')

class RegisterView(View) :

    def get(self,request) : 
        return render(request , 'accounts/register.html')

    def post(self, request) : 
        fname = request.POST.get('first_name') 
        lname = request.POST.get('last_name') 
        email = request.POST.get('email')
        password = request.POST.get('password')
    
        user  = get_user_model().objects.filter(username= email)
        if user.exists() : 
            messages.warning(request ,'This email is already taken')
            return render(request , 'accounts/register.html')
        
        user = get_user_model().objects.create(first_name = fname , email = email , last_name = lname , username = email)
        user.set_password(password)
        user.save()

        messages.success(request ,"Please log in to continue")
        return redirect(reverse('accounts:login'))
    

class LogoutView(View) : 

    def get(self ,request) : 
        logout(request)
        return redirect(reverse('accounts:login'))
    

class AddToCartView(LoginRequiredMixin ,View) :


    def get(self ,request, uid) : 

        product = Product.objects.get(uid = uid)
        cart ,created  = Cart.objects.get_or_create(user = self.request.user , is_paid = False)
        cartItem = CartItems.objects.create(cart = cart  ,product  =product)
        size =  request.GET.get('size')
        if size : 
            size_variant =SizeVariant.objects.get(size_name = size)
            cartItem.size_variant = size_variant
            cartItem.save()
        
        messages.success(request ,'Product added to cart successfully')
        return redirect(request.META.get('HTTP_REFERER'))
    

class CartView(LoginRequiredMixin ,  View) : 


    def get(self , request) : 
        cart = Cart.objects.get(is_paid = False ,user = self.request.user)
        sum = cart.get_cart_total()
        if cart.coupon : 
            sum -= cart.coupon.discount_price

        client = razorpay.Client(auth=( settings.RAZOR_PAY_KEY_ID , settings.RAZOR_PAY_KEY_SECRET))

        data = { "amount": sum, "currency": "INR", "receipt": "order_rcptid_11" }
        payment = client.order.create(data=data)

        cart.razor_pay_order_id = payment['id']
        cart.save()

        print(payment)
        context  = {
            'cart' : cart , 'sum' : sum , 'payment' : payment
        }
        return render(request , 'accounts/cart.html' , context)

    
    def post(self , request) : 

        cart = Cart.objects.get(is_paid = False , user = self.request.user)
        coupon = request.POST.get('coupon')  
        coupon_obj = Coupon.objects.filter(coupon_code__icontains = coupon)

        if not coupon_obj.exists() : 
            messages.warning(request ,'Invalid coupon')
            return redirect(request.META.get('HTTP_REFERER'))
        
        if cart.coupon : 
            messages.warning(request ,'Coupon already applied')
            return redirect(request.META.get('HTTP_REFERER'))
        
        cart_total = cart.get_cart_total()

        if cart_total < coupon_obj[0].minimum_amount : 
            messages.warning(request , f'Minimum Amount must be {coupon_obj[0].minimum_amount}')
            return redirect(request.META.get('HTTP_REFERER'))
        
        if coupon_obj[0].is_expired : 
            messages.warning(request , 'Coupon has expired')
            return redirect(request.META.get('HTTP_REFERER'))
           

        cart.coupon = coupon_obj[0]
        cart.save()
        messages.success(request , 'Coupon applied')
        return redirect(request.META.get('HTTP_REFERER'))

class RemoveCartItemView(View) : 

    def get(self,request , cartItem_uid) : 

        cart_item = CartItems.objects.get(uid = cartItem_uid)
        cart_item.delete()        
        return redirect(request.META.get('HTTP_REFERER'))

class RemoveCouponView(View) : 

    def get(self,request , cart_id) :

        cart = Cart.objects.get(uid = cart_id)
        cart.coupon = None
        cart.save()
        messages.success(request , 'Coupon removed successfully')
        return redirect(request.META.get('HTTP_REFERER'))


        
        
        
            
        
