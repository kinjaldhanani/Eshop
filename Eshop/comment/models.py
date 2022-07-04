import datetime
from django.db import models
from product.models import Product
from user_info.models import User


class Comment(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='comment_user')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    date = models.DateField(default=datetime.date.today)
    comment = models.CharField(max_length=200)
