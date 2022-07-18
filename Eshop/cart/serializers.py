#
# from rest_framework import serializers, request
# from rest_framework.generics import get_object_or_404
# from cart.models import Cart, Item
# from order.models import OrderItem, Order
# from product.models import Product
#
#
# class ItemSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(required=False)
#
#     class Meta:
#         model = Item
#         fields = ['id','cart','quantity','product','get_total']
#         extra_kwargs = {'cart': {'required': False}}
#
# class CartSerializer(serializers.ModelSerializer):
#     items = ItemSerializer(many=True)
#
#     class Meta:
#         model = Cart
#         fields = ['id','customer','items','total']
#         read_only_fields = ['date','status']
#
#     def create(self, validated_data):
#         cart_data = validated_data.pop('items')
#         validated_data['customer'] = self.context['request'].user
#         cart = super().create(validated_data)
#         for data in cart_data:
#             product_id = data.get('product').id
#             data.update({
#                 'product': product_id,
#                 'quantity': data.get('quantity'),
#                 'cart': cart.id,
#
#             })
#             cart_serializer = ItemSerializer(data=data)
#             cart_serializer.is_valid(raise_exception=True)
#             cart_serializer.save()
#         return cart
#
#     def update(self, instance, validated_data):
#         orders_data = validated_data.pop('items')
#         instance.customer = validated_data.get('customer', instance.customer)
#         for data in orders_data:
#             if item := instance.items.filter(id=data.get('id')).first():
#                 item.product = data.get('product')
#                 item.quantity = data.get('quantity')
#                 item.save()
#                 instance.save()
#             else:
#                 product_id = data.get('product').id
#                 data.update({
#                     'product': product_id,
#                     'quantity': data.get('quantity'),
#                     'cart': instance.id,
#
#                 })
#                 order_serializer = ItemSerializer(data=data)
#                 order_serializer.is_valid(raise_exception=True)
#                 order_serializer.save()
#             instance.items.clear()
#         return instance
#


from rest_framework import serializers
from cart.models import Cart, Item


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id','customer','total']
        read_only_fields = ['date','status']


class ItemSerializer(serializers.ModelSerializer):
    items = CartSerializer(many=True, required=True)

    class Meta:
        model = Item
        fields = ['id','items','quantity','product','get_total']
        extra_kwargs = {'items': {'required': False}}

    def create(self, validated_data):
        questions_data = validated_data.pop('items')
        item = Item.objects.create(**validated_data)
        for question in questions_data:
            Cart.objects.create(exam=item, **question)
        return item




