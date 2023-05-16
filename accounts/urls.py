from django.urls import path ,include 
from django.views.generic import TemplateView
from .views import (
    LoginView ,
    RegisterView ,
    LogoutView ,
    AddToCartView ,
    CartView ,
    RemoveCartItemView,
    RemoveCouponView ,
    SuccessView
)

app_name = 'accounts'

urlpatterns = [
    path('' , TemplateView.as_view(template_name = 'core/base.html') , name = 'home' ) ,
    path('login/' , LoginView.as_view() , name = 'login'),
    path('register/' , RegisterView.as_view() , name = 'register'),
    path('logout/' , LogoutView.as_view() , name  = 'logout') ,
    path('add_to_cart/<uuid:uid>' , AddToCartView.as_view() , name = 'add-to-cart') ,
    path('cart/' , CartView.as_view() , name = 'cart') ,
    path('remove-cart-item/<uuid:cartItem_uid>' , RemoveCartItemView.as_view() , name = 'remove-cart-item') ,
    path('remove-coupon/<uuid:cart_id>' , RemoveCouponView.as_view() ,name = 'remove-coupon'),
    path('success/' , SuccessView.as_view() ,name = 'payment-success'),
]
