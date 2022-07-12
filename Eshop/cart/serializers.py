from rest_framework import serializers
from cart.models import Cart, Item


class ItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Item
        fields = ['id','cart','quantity','product','get_total']
        extra_kwargs = {'cart': {'required': False}}


class CartSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['id','customer','items','total']
        read_only_fields = ['date','status']

    def create(self, validated_data):
        cart_data = validated_data.pop('items')
        cart = super().create(validated_data)
        for data in cart_data:
            product_id = data.get('product').id
            data.update({
                'product': product_id,
                'quantity': data.get('quantity'),
                'cart': cart.id,

            })
            order_serializer = ItemSerializer(data=data)
            order_serializer.is_valid(raise_exception=True)
            order_serializer.save()
        return cart

    def update(self, instance, validated_data):
        orders_data = validated_data.pop('items')
        instance.customer = validated_data.get('customer', instance.customer)
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
                    'cart': instance.id,

                })
                order_serializer = ItemSerializer(data=data)
                order_serializer.is_valid(raise_exception=True)
                order_serializer.save()
        return instance







