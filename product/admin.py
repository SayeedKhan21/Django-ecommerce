from django.contrib import admin
from .models import * 
# Register your models here.


admin.site.register(Category)

class ProductImageAdmin(admin.StackedInline) : 
    model = ProductImage


class ProductAdmin(admin.ModelAdmin)  : 
    list_display = ['product_name' , 'price']
    inlines = [ProductImageAdmin]

admin.site.register(Product , ProductAdmin)

admin.site.register(ColorVariant)
admin.site.register(SizeVariant)


class CartAdmin(admin.ModelAdmin) : 
    list_display = ['user' , 'is_paid']
admin.site.register(Cart ,CartAdmin)


class CartItemsAdmin(admin.ModelAdmin) : 
    list_display = ['cart' , 'product' , 'size_variant']
admin.site.register(CartItems , CartItemsAdmin)

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin) : 
    list_display = [ 'discount_price' , 'minimum_amount']


admin.site.register(ProductImage)
