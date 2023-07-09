from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User


class customer(models.Model):
    # firstname = models.CharField(max_length=50)
    # lastname = models.CharField (max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    phone = models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    # email=models.EmailField()
    # password = models.CharField(max_length=100)
    def __str__(self):
        return self.phone

class category(models.Model):
    categoryname=models.CharField(max_length=225)

    def __str__(self):
        return self.categoryname

class Brand(models.Model):
        Brand=models.CharField(max_length=255)

        def __str__(self):
            return self.Brand

    
    
class product(models.Model):
    category=models.ForeignKey(category,on_delete=models.CASCADE,blank=True,null=True)
    Brand=models.ForeignKey(Brand,on_delete=models.CASCADE,blank=True,null=True)
    image=models.ImageField(upload_to='image/',null=True,blank=True)
    name=models.CharField(max_length=25)
    description=models.CharField(max_length=255,unique=True)
    price=models.IntegerField(blank=True,null=True)
    stock=models.IntegerField(blank=True,null=True)
    # available=models.BooleanField(default=True)
    # created=models.DateTimeField(auto_now_add=True)
    # updated=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
class Order(models.Model):
    product = models.ForeignKey(product,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=True,null=True)
    price = models.IntegerField()
    address = models.CharField (max_length=50, default='', blank=True)
    phone = models.CharField (max_length=50, default='', blank=True)
    # date = models.DateField (default=datetime.datetime.today)
    status = models.BooleanField (default=False)
    
# class cart(models.Model):
#     product = models.ForeignKey(product,on_delete=models.CASCADE)
#     user=models.ForeignKey(User,on_delete=models.CASCADE)   
#     quantity = models.IntegerField()
#     def sub_total(self):
#         return self.product.price * self.quantity      
#     def __str__(self):
#         return self.product.name
    