# from django.contrib import admin
#
# from cart.models import Cart, Item
#
#
# @admin.register(Item)
# class ItemAdmin(admin.ModelAdmin):
#     list_display = ['id', 'quantity']
#
#
# @admin.register(Cart)
# class CartAdmin(admin.ModelAdmin):
#     list_display = ['id','customer', 'date','status']

from django.contrib import admin

from cart.models import Cart, Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'quantity', 'item']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id','customer', 'date','status']
