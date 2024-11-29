from django.contrib import admin


# from django.contrib.admin import ModelAdmin
from .models import Product,Market 
# , Borrow
#  Logistics, Rdv

admin.site.register(Product)
admin.site.register(Market )
# admin.site.register(Consumer)

# admin.site.register(Borrow)

