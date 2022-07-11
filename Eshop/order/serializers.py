

from rest_framework import serializers

import order
from order.models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ["order","product", "quantity", "total_cost"]
        extra_kwargs = {'order': {'required': False}}


class OrderSerializer(serializers.ModelSerializer):
    OrderItems = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id", "customer", "address", "phone", "OrderItems", "get_total"]
        read_only_fields = ["date", "id"]

    def create(self, validated_data):
        orders_data = validated_data.pop('OrderItems')
        order = super().create(validated_data)
        for data in orders_data:
            item = dict()
            product_id = data.get('product').id
            item.update({
                'product': product_id,
                'quantity': data.get('quantity'),
                'order': order.id,

            })
            order_serializer = OrderItemSerializer(data=item)
            order_serializer.is_valid(raise_exception=True)
            order_serializer.save()
        return order

    def update(self, instance, validated_data):
        # instance = super().update(instance, validated_data)
        OrderItems = validated_data.pop('OrderItems')
        instance.customer = validated_data.get('customer', instance.customer)
        instance.address = validated_data.get('address', instance.address)
        instance.phone = validated_data.get('phone', instance.phone)
        for data in OrderItems:
            if item := instance.OrderItems.filter(id=data.get('id')).first():
                item.product = data.get('product')
                item.quantity = data.get('quantity')
                item.save()
            else:
                order = super().create(validated_data)
                product_id = data.get('product').id
                data.update({
                    'product': product_id,
                    'quantity': data.get('quantity'),
                    'order': order.id,

                })
                order_serializer = OrderItemSerializer(data=data)
                order_serializer.is_valid(raise_exception=True)
                order_serializer.save()
                return order
        return instance