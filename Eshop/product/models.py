from django.db import models
from category.models import Category
from user_info.models import User
from django.db.models import signals
from django.dispatch import receiver





class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)




