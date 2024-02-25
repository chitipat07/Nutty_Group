from django.contrib import admin
from .models import Menu, Basket, BasketItem, Order


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')

class BasketAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price', 'created_at')

class BasketItemAdmin(admin.ModelAdmin):
    list_display = ('menu', 'basket', 'quantity')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('basket', 'user','menu_item','total_price','quantity', 'created_at', 'table_number', 'note')

admin.site.register(Menu, MenuAdmin)
admin.site.register(Basket, BasketAdmin)
admin.site.register(BasketItem, BasketItemAdmin)
admin.site.register(Order, OrderAdmin)