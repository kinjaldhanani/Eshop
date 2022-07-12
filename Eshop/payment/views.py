import stripe
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from order.models import Order
from payment.models import Payment
from payment.serializers import PaymentSerializer

stripe.api_key = 'sk_test_51LKfHrSEHBoQx2VY7BE7sQEJpRIVpFBLk03k3prYxjJj3B1PVJn5R0yBaU8b53zo59lQLgBhiH79m65aXwSCZ6Ek00CZIFAwwR'


class PaymentView(ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated]

    def test_payment(self):
        test_payment_intent = stripe.PaymentIntent.create(
            amount=54890,
            currency='pln',
            payment_method_types=['card'],
            receipt_email='kinjal.dhanani@trootech.com')

        return Response(status=status.HTTP_200_OK, data=test_payment_intent)



