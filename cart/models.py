from django.db import models
from productsapp.models import product
from django.contrib.auth.models import User


    
class CartItem(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)    
    # cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField(blank=True,null=True)
    active=models.BooleanField(default=True)
    
    
    class Meta:
        db_table='CartItem'
            
    def sub_total(self):
        return self.product.price * self.quantity 
    def __str__(self):
        return '{}'.format(self.product)   
        
    
    
