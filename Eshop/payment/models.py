from django.db import models

# Create your models here.
from dynaconf import settings

from order.models import Order
from user_info.models import User


class Payment(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE, related_name='orders')
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

