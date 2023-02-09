from django.urls import path ,include
from .views import (
    ProductDetailView ,
)
urlpatterns = [
    path('<slug>/' , ProductDetailView.as_view() , name = 'product-detail')
]
