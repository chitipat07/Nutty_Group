from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='image/')

    def __str__(self):
        return f'{self.name} {self.price} {self.image}'


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} {self.total_price} {self.created_at}'

    @property
    def get_basket_total(self):
        basketitems = self.basketitem_set.all()
        total = sum([item.get_total for item in basketitems])
        return total
    
    @property
    def get_basket_items(self):
        basketitems = self.basketitem_set.all()
        total = sum([item.quantity for item in basketitems])
        return total
    
    @property
    def get_basket_items_list(self):
        basketitems = self.basketitem_set.all()
        return basketitems


class BasketItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    @property
    def get_total(self):
        total = self.menu.price * self.quantity
        return total

class Order(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_item = models.CharField(max_length=250, blank=True, null=True)
    total_price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    table_number = models.IntegerField(default=0)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.basket} {self.user} {self.total_price} {self.created_at} {self.table_number} {self.note}'

    # @property
    # def get_basket_items(self):
    #     basketitems = self.basket.basketitem_set.all()
    #     return basketitems
