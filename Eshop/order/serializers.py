from rest_framework import serializers
from rest_framework.templatetags.rest_framework import data

from order.models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'total_cost']


class OrderSerializer(serializers.ModelSerializer):
    OrderItems = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'address', 'phone', 'OrderItems', 'get_total']
        read_only_fields = ['date']

    # def create(self, validated_data):
    #     order_items = validated_data.pop('OrderItems')
    #     parent = Order.objects.create(**validated_data)
    #     for data in order_items:
    #         parent.order_items.create(**data)
    #     return parent

    def create(self, validated_data):
        import pdb; pdb.set_trace()
        order_items = validated_data.pop('OrderItems')
        if validated_data.get('OrderItems'):
            order_serializer = OrderItemSerializer(data=order_items)
            if order_serializer.is_valid():
                order_serializer.save()
        return super(OrderSerializer, self).create(validated_data)


# def update(self, instance, validated_data):
#         if validated_data.get('OrderItems'):
#             order_data = validated_data.get('quantity')
#             order_serializer = OrderItemSerializer(data=order_data)
#             if order_serializer.is_valid():
#                 order = order_serializer.update(instance=instance.profile,validated_data=order_serializer.validated_data)
#                 validated_data['OrderItems'] = order
#         return super().update(instance, validated_data)










