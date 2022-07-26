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
    likes = models.ManyToManyField(User, default=None, related_name='blogpost_like', null=True, blank=True)

    def __str__(self):
        return self.name

    def number_of_likes(self):
        return self.likes.count()

    # @receiver(signals.pre_save, sender=Product)
    # def check_product_description(sender, instance, **kwargs):
    #     if not instance.description:
    #         instance.description = 'This is Default Description'
