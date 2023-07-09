# from cart.models import CartItem


# def counter(request):
#     item_count=0
#     if 'admin' in request.path:
#         return {} 
#     else:
#         try:
#           user=request.user
            
#           cart_items=CartItem.objects.filter(user=user)
#           for cart_item in cart_items:
#             item_count+=cart_item.quantity
#         except CartItem.DoesNotExist:
#             return dict(item_count=item_count) 
            
#     return dict(item_count=item_count)        
            