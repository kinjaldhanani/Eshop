import stripe
from rest_framework import serializers
from order.models import Order, OrderItem

stripe.api_key = 'sk_test_51LKfHrSEHBoQx2VY7BE7sQEJpRIVpFBLk03k3prYxjJj3B1PVJn5R0yBaU8b53zo59lQLgBhiH79m65aXwSCZ6Ek00CZIFAwwR '


class OrderItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = OrderItem
        fields = ["id", "order", "product", "quantity", "total_cost"]
        extra_kwargs = {'order': {'required': False}}


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id","customer","address", "phone", "items", "total_amount"]
        read_only_fields = ["date", "id"]

    def create(self, validated_data):
        orders_data = validated_data.pop('items')
        validated_data['customer'] = self.context['request'].user
        order = super().create(validated_data)
        for data in orders_data:
            product_id = data.get('product').id
            data.update({
                'product': product_id,
                'quantity': data.get('quantity'),
                'order': order.id,

            })
            order_serializer = OrderItemSerializer(data=data)
            order_serializer.is_valid(raise_exception=True)
            order_serializer.save()
        order.set_amount()
        return order


