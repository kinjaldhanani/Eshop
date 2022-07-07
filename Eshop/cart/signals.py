from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from cart.models import Cart
from order.models import Order


@receiver(post_save, sender=Order)
def delete_related_cart(sender, instance, **kwargs):
     cart = Cart.objects.filter(customer=instance.customer)
     cart.delete()







