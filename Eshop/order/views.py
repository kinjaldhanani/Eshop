
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from Eshop.permissions import IsOwner
from order.models import Order
from order.serializers import OrderSerializer
import stripe

stripe.api_key = 'sk_test_51LKfHrSEHBoQx2VY7BE7sQEJpRIVpFBLk03k3prYxjJj3B1PVJn5R0yBaU8b53zo59lQLgBhiH79m65aXwSCZ6Ek00CZIFAwwR '


def test_payment():
    stripe.PaymentIntent.create(
        amount=2000,
        currency="usd",
        payment_method_types=["card"],
    )


class OrderView(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        """Show only authenticate user order"""
        if self.request.user.is_authenticated:
            return Order.objects.filter(customer=self.request.user.id)

    test_payment()


