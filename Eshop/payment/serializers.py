import stripe
from rest_framework import serializers

from payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['order', 'customer', 'amount']
        extra_kwargs = {'date': {'required': False}}

    # def create(self, validated_data):
    #     test_payment_intent = stripe.PaymentIntent.create(
    #         amount=54890, currency='pln',
    #         payment_method_types=['card'],
    #         receipt_email='kinjal.Dhanani@trootech.com')
    #     return test_payment_intent