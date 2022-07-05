# from django.db import models
# from product.models import Product
# from user_info.models import User
# import datetime
#
#
# class Cart(models.Model):
#     """A model that contains data for a shopping cart."""
#     customer = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart', null=True, blank=True)
#     date = models.DateField(default=datetime.date.today)
#     status = models.BooleanField(default=True, null=True, blank=True)
#
#     @property
#     def total(self):
#         total = 0
#         for item in self.items.all():
#             total += item.get_total()
#         return total
#
#
# class Item(models.Model):
#     """A model that contains data for an item in the shopping cart."""
#     cart = models.ForeignKey(
#         Cart,
#         related_name='items',
#         on_delete=models.CASCADE,
#         null=True,
#         blank=True
#     )
#     product = models.ForeignKey(
#         Product,
#         related_name='items',
#         on_delete=models.CASCADE, null=True, blank=True
#     )
#     quantity = models.PositiveIntegerField(default=1, null=True, blank=True)
#
#     def get_total(self):
#         return self.quantity * self.product.price

from django.db import models
from product.models import Product
from user_info.models import User
import datetime


class Item(models.Model):
    quantity = models.IntegerField(default=0)
    item = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items', null=True, blank=True)

    def total_cost(self):
        return self.quantity * self.item.price


class Cart(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE, default='1', null=True, blank=True)
    date = models.DateField(default=datetime.date.today)
    status = models.BooleanField(default=True, null=True, blank=True)
    product = models.ManyToManyField(Item, default='1', null=True, blank=True, related_name="items")

    @property
    def get_total(self):
        total = 0
        for item in self.product.all():
            total += item.total_cost()
        return total


