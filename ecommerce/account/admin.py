from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Profile)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_paid']
    model = Cart

@admin.register(CartItems)
class CartItemsAdmin(admin.ModelAdmin):
    list_display = ['cart', 'product', 'size_variant', 'color_variant', 'quantity']
    model = CartItems
