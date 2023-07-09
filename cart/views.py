from django.shortcuts import render,redirect,get_object_or_404
from productsapp.models import product
from .models import CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import auth,User
from productsapp.views import*

def add_cart(request,product_id):
   
    prod=product.objects.get(id=product_id)
    user=User(id=request.user.id)

    print(prod)
    try:
        cart_item=CartItem.objects.get(product=prod,user=user)
        if cart_item.quantity < cart_item.product.stock: 
            cart_item.quantity += 1
            cart_item.save()
    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(product=prod,quantity=1,user=user)
        cart_item.save()
        
    return redirect('cart:cart_detail') 
def cart_detail(request,total=0,counter=0,cart_items=None):
    if 'username'in request.session:
        
        try:
            user=request.user
            
            cart_items=CartItem.objects.filter(user=user)
            for cart_item in cart_items: 
                total +=(cart_item.product.price * cart_item.quantity)
                counter +=cart_item.quantity
        except CartItem.DoesNotExist:
            pass
        #print(cart_items)
        return render(request,'cartnew.html',dict(cart_items=cart_items,total=total,counter=counter))  
    else:
       return redirect(login_user)      
               
def cart_remove(request,product_id):
   
        
   
    prod=get_object_or_404(product,id=product_id)
    cart_item=CartItem.objects.get(product=prod)
    print(cart_item.quantity)
    
                
    if cart_item.quantity > 1:  
        cart_item.quantity -=1
        cart_item.save()
        
    else:
        cart_item.delete()
    return redirect('cart:cart_detail')

def full_remove(request,product_id):
  
        
   
   
    prod=get_object_or_404(product,id=product_id)
    cart_item=CartItem.objects.filter(product=prod)
    cart_item.delete()
    return redirect('cart:cart_detail')

    
               
        
    

