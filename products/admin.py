from django.contrib import admin
from .models import Product, Image, Brand

admin.site.register(Brand)
admin.site.register(Image)
admin.site.register(Product)
