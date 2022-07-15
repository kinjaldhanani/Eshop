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
    # total_amount = serializers.IntegerField(source="get_total", read_only=True)

    class Meta:
        model = Order
        fields = ["id", "customer", "address", "phone", "items", "total_amount"]
        read_only_fields = ["date", "id"]

    def create(self, validated_data):
        orders_data = validated_data.pop('items')
        order = super().create(validated_data)

        customer = validated_data.get("customer")
        Order.objects.create(customer=customer, **validated_data)
        
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
            order.save()
        return order



    def update(self, instance, validated_data):
        orders_data = validated_data.pop('items')
        instance.customer = validated_data.get('customer', instance.customer)
        instance.address = validated_data.get('address', instance.address)
        instance.phone = validated_data.get('phone', instance.phone)
        for data in orders_data:
            if item := instance.items.filter(id=data.get('id')).first():
                item.product = data.get('product')
                item.quantity = data.get('quantity')
                item.save()
                instance.save()
            else:
                product_id = data.get('product').id
                data.update({
                    'product': product_id,
                    'quantity': data.get('quantity'),
                    'order': instance.id,

                })
                order_serializer = OrderItemSerializer(data=data)
                order_serializer.is_valid(raise_exception=True)
                order_serializer.save()
        return instance

