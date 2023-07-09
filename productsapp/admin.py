from django.contrib import admin
from productsapp.models import category,product,Order,customer
# Register your models here.
admin.site.register(category)
admin.site.register(product)
admin.site.register(Order)
admin.site.register(customer)

# admin.site.register(cart)
# admin.site.register(Brand)
