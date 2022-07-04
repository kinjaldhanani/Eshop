from abc import ABC

from rest_framework import serializers

import product
from product import models
from product.models import Product


class ProductListSerializer(serializers.ListSerializer):

    def create(self, validated_data):
        products = [models.Product(**category) for category in validated_data]
        return models.Product.objects.bulk_create(products)

    def update(self, instance, validated_data):
        ret = []
        for data in validated_data:
            if "id" in data and data['id'] not in ['', None]:
                Product.objects.filter(id=data['id']).update(**data)
                ret.append(data)
            else:
                ret.append(Product.objects.create(**data))
        return ret





class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Product
        list_serializer_class = ProductListSerializer
        fields = ['id', 'name', 'category', 'description', 'price', 'image']



class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'image']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'likes']
