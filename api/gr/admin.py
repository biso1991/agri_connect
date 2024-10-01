from django.contrib import admin


# from django.contrib.admin import ModelAdmin
from .models import Product, Logistics, Rdv
# , Borrow


admin.site.register(Product)
admin.site.register(Logistics)
admin.site.register(Rdv)

# admin.site.register(Borrow)

