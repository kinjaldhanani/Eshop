from rest_framework import serializers
from cart.models import Cart, Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'cart', 'quantity', 'product', 'get_total']

    def create(self, validated_data):
        user = self.context['request'].user
        obj, created = Cart.objects.get_or_create(customer=user)
        if created:
            obj.save()
        validated_data.update({
            'product': validated_data.get('product'),
            'quantity': validated_data.get('quantity'),
            'cart': obj,
        })
        return super().create(validated_data)
