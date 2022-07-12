from rest_framework import serializers

from category.models import Category


class SubCategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Category
        fields = ('id', 'parent','name', 'description')


class CategorySerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=True, read_only=False)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'subcategory']

    def create(self, validated_data):
        category = validated_data.pop('subcategory')
        parent = super().create(validated_data)
        for data in category:
            data.update({
                'name': data.get('name'),
                'description': data.get('description'),
                'parent': parent.id,

            })
            order_serializer = SubCategorySerializer(data=data)
            order_serializer.is_valid(raise_exception=True)
            order_serializer.save()
        return parent

    def update(self, instance, validated_data):
        sub_category = validated_data.pop('subcategory')
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        for data in sub_category:
            if sub := instance.subcategory.filter(id=data.get('id')).first():
                sub.name = data.get("name")
                sub.description = data.get("description")
                sub.save()
            else:
                data.update({
                    'name': data.get('name'),
                    'description': data.get('description'),
                    'parent': instance.id,
                })
                order_serializer = SubCategorySerializer(data=data)
                order_serializer.is_valid(raise_exception=True)
                order_serializer.save()
        return instance