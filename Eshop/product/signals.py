from django.db.models import signals
from django.dispatch import receiver

from .models import Product

"""pre_save method signal"""


@receiver(signals.pre_save, sender=Product)
def check_product_description(sender, instance, **kwargs):
    if not instance.description:
        instance.description = 'This is Default Description'


"""post_save method signal"""


@receiver(signals.post_save, sender=Product)
def create_product(sender, instance, created, **kwargs):
    print("Save method is called")
