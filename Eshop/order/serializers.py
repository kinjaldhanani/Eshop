from django.core.paginator import Page
from rest_framework import serializers, request
from rest_framework.templatetags.rest_framework import data

from order.models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["product", "quantity", "total_cost"]


class OrderSerializer(serializers.ModelSerializer):
    OrderItems = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id", "customer", "address", "phone", "OrderItems", "get_total"]
        read_only_fields = ["date"]

    # def create(self, validated_data):
    #
    #     order_items = validated_data.pop('OrderItems')
    #     parent = Order.objects.create(**validated_data)
    #     for data in order_items:
    #         parent.OrderItems.create(**data)
    #     return parent

    def create(self, validated_data):

        orders_data = validated_data.pop('OrderItems')
        parent = Order.objects.create(**validated_data)
        for data in orders_data:
            order_serializer = OrderItemSerializer(data=data, many=True)
            order_serializer.is_valid(raise_exception=True)
            orders = order_serializer.save()
            orders.parent = parent
            orders.save()
        return parent


# def update(self, instance, validated_data):
#         if validated_data.get('OrderItems'):
#             order_data = validated_data.get('quantity')
#             order_serializer = OrderItemSerializer(data=order_data)
#             if order_serializer.is_valid():
#                 order = order_serializer.update(instance=instance.profile,validated_data=order_serializer.validated_data)
#                 validated_data['OrderItems'] = order
#         return super().update(instance, validated_data)
