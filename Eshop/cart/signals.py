from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from stripe.api_resources.payment_intent import PaymentIntent

from cart.models import Cart
from order.models import Order, OrderItem


@receiver(post_save, sender=Order)
def delete_related_cart(sender, instance, **kwargs):
    cart = Cart.objects.filter(customer=instance.customer)
    cart.delete()


# @receiver(post_save, sender=Order)
# def delete_related_cart(sender, instance, **kwargs):
#     payment = PaymentIntent.create(
#         amount=instance.set_amount(),
#         currency="usd",
#         payment_method_types=["card"],
#     )
#     payment.save()


