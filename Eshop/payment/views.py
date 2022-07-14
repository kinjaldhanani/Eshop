
import stripe
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from order.models import Order
from payment.models import Payment
from payment.serializers import PaymentSerializer

stripe.api_key = 'sk_test_51LKfHrSEHBoQx2VY7BE7sQEJpRIVpFBLk03k3prYxjJj3B1PVJn5R0yBaU8b53zo59lQLgBhiH79m65aXwSCZ6Ek00CZIFAwwR '


# def test_payment():
#     stripe.PaymentIntent.create(
#         amount=1,
#         currency="usd",
#         payment_method_types=["card"],
#     )

class PaymentView(ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        order = Order.objects.get(customer=self.request.user, ordered=False)
        amount = int(order.get_total())
        stripe.PaymentIntent.create(
            amount=amount,
            currency="usd",
            payment_choice=["card"],
        )
        order.save()




