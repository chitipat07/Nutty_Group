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


class BasketItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.menu} {self.basket} {self.quantity}'

class Order(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    table_number = models.IntegerField(default=0)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.basket} {self.user} {self.total_price} {self.created_at} {self.table_number} {self.note}'