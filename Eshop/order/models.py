
from django.db import models
from product.models import Product
from user_info.models import User
import datetime


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50,blank=True)
    date = models.DateField(default=datetime.date.today)

    @property
    def get_total(self):
        total = 0
        for item in self.order_items.all():
            total += item.total_cost()
        return total


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='OrderItems')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_order', default=1)
    quantity = models.IntegerField()

    def total_cost(self):
        return self.quantity * self.product.price



