from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, default='1')
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="sub_category")

    def __str__(self):
        return self.name
