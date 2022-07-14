
from rest_framework import serializers
from payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['order', 'customer', 'amount', 'currency', 'payment_choice']
        extra_kwargs = {'transection_date': {'required': False}, 'amount': {'required': False}}

