from django.db import models
from core.models import (
    BaseModel ,
)
from django.utils.text import slugify
from django.conf import settings

# Create your models here.

class Category(BaseModel) : 
    category_name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True ,null = True , blank = True)
    category_image = models.ImageField(upload_to='categories')

    class Meta : 
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        return self.category_name

    def save(self ,*args, **kwargs) : 
        self.slug = slugify(self.category_name)
        return super().save(*args , **kwargs)
    
class ColorVariant(BaseModel) : 
    color_name = models.CharField(max_length=10)
    color_price = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.color_name

class SizeVariant(BaseModel) :
    size_name = models.CharField(max_length=5)
    size_price = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.size_name

class Product(BaseModel)  :
    product_name = models.CharField(max_length=255)
    category = models.ForeignKey(Category , on_delete=models.CASCADE , related_name='product_category')
    price = models.IntegerField()
    product_description = models.TextField()
    slug = models.SlugField(unique=True ,null = True , blank = True)
    color = models.ManyToManyField(ColorVariant , blank=True)
    size = models.ManyToManyField(SizeVariant ,blank=True)

    def save(self,*args, **kwargs) : 
        self.slug = slugify(self.product_name)
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.product_name
    
    def get_product_correct_price(self ,sz) : 
        price = self.price 
        if sz : 
            price += SizeVariant.objects.get(size_name =sz).size_price
        return price
    


class ProductImage(BaseModel) : 
    product = models.ForeignKey(Product ,  on_delete=models.CASCADE ,related_name='product_images')
    image = models.ImageField(upload_to='products')

class Coupon(BaseModel) : 

    coupon_code = models.CharField(max_length = 10 )
    is_expired = models.BooleanField(default = False)
    discount_price  = models.IntegerField(default = 100)
    minimum_amount  = models.IntegerField(default = 500)

    def __str__(self) -> str:
        return self.coupon_code



class Cart(BaseModel) : 
    user = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE , related_name='cart')
    is_paid = models.BooleanField(default=False)
    coupon = models.ForeignKey(Coupon , on_delete=models.SET_NULL , null = True , blank = True)
    razor_pay_order_id = models.CharField(max_length=100 , null= True ,blank = True)
    razor_pay_payment_id= models.CharField(max_length=100 , null= True ,blank = True)
    razor_pay_payment_signature = models.CharField(max_length=100 , null= True ,blank = True)

    def __str__(self) -> str:
        return str(self.user)
    
    def get_total_cart_items(self) : 

        """ Returns the total number of cart Items for a particular cart using Reverse Manager """

        return self.cart_items.count()
    
    def get_cart_total(self):

        price =  []
        for item in self.cart_items.all() : 
            if item.size_variant : 
                price.append(item.product.get_product_correct_price(item.size_variant))
            else :
                price.append(item.product.price)
        return sum(price)


class CartItems(BaseModel) : 
      cart = models.ForeignKey(Cart ,on_delete=models.CASCADE ,related_name="cart_items")
      product = models.ForeignKey(Product , on_delete=models.SET_NULL , null=True , blank=True)
      size_variant = models.ForeignKey(SizeVariant ,on_delete=models.SET_NULL , null=True ,blank  =True)

      class Meta : 
          verbose_name_plural = 'Cart Items'

        
      def get_product_price(self) : 
          
        """ Get correct price of the product associated with item """

        price = self.product.price
        if self.size_variant : 
              price += (SizeVariant.objects.get(size_name = self.size_variant)).size_price
        return price
               