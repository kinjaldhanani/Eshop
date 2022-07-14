

from django.db import models
from django_extensions.db.models import TimeStampedModel
from order.models import Order
from user_info.models import User


class Payment(TimeStampedModel):
    CARD = "card"
    CASE_ON_DELIVERY = "case_on_delivery"

    PAYMENT_METHOD = (
        (CARD, "card"),
        (CASE_ON_DELIVERY, "case_on_delivery"),

    )
    order = models.ForeignKey(Order,on_delete=models.CASCADE, related_name='payments', blank=True, null=True)
    customer = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_payments', blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    transection_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    currency = models.CharField(max_length=20, blank=True, null=True)
    payment_choice = models.CharField(max_length=20, choices=PAYMENT_METHOD, blank=True, null=True)



