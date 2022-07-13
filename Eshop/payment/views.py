import stripe
from rest_framework import status, request
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


    # def payment(request):
    #     order = Order.objects.get(customer=request.user, ordered=False)
    #     amount = int(order.get_total() * 100)
    #
    #     if request.method == 'POST':
    #         print(" request is post ")
    #         order_amount = amount,
    #         order_currency = "INR",
    #         order_receipt = 'order_rcptid_11'
    #         course = client.order.create(dict(amount=order_amount,
    #                                           currency=order_currency,
    #                                           receipt=order_receipt,
    #                                           payment_capture='0'))
    #         context = {}
    #         context['order_id'] = course['id']
    #         return context