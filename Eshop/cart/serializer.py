# from rest_framework import serializers
# from cart.models import Cart, Item
#
#
# class CartSerializer(serializers.ModelSerializer):
#     # total = serializers.SerializerMethodField(source='get_total', read_only=True)
#
#     class Meta:
#         model = Cart
#         fields = ['id','customer','total']
#         read_only_fields = ['date','status']
#
#
# class ItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Item
#         fields = ['id', 'quantity','cart','product','get_total']


from rest_framework import serializers
from cart.models import Cart, Item


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'product','get_total']
        read_only_fields = ['date','status']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'quantity', 'item','total_cost']