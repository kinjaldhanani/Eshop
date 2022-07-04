from django.db import models
from product.models import Product
from user_info.models import User
import datetime


class Item(models.Model):
    quantity = models.IntegerField(default=0)
    item = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')

    def total_cost(self):
        return self.quantity * self.item.price


class Cart(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE, default='1')
    date = models.DateField(default=datetime.date.today)
    status = models.BooleanField(default=True)
    product = models.ManyToManyField(Item, default='1')

    @property
    def get_total(self):
        total = 0
        for item in self.product.all():
            total += item.total_cost()
        return total
