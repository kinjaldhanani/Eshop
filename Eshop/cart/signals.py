from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from rest_framework.decorators import action

import cart
from cart.models import Cart, Item
from order.models import Order


# @receiver(post_save, sender=Order)
# def delete_related_cart(sender, instance, **kwargs):
#     cart = Cart.objects.filter(customer=instance.customer)
#     cart.delete()



from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from cart.models import Cart
from order.models import Order


@receiver(post_save, sender=Order)
def delete_related_cart(sender, instance, **kwargs):
    import pdb; pdb.set_trace()

    cart = Cart.objects.filter(customer=instance.customer)
    cart.delete()
    item = cart.items.all()
    item.delete()


# @receiver(m2m_changed, sender=Order.product.through)
# def delete_related_cart(sender, instance, **kwargs):
#     if action == 'post_remove':
#         item = Item.objects.all()
#         item.delete()


