from rest_framework import serializers

from category.models import Category


class sub_categorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class CategorySerializer(serializers.ModelSerializer):
    sub_category = sub_categorySerializer(many=True, read_only=False)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'sub_category']

    def create(self, validated_data):
        sub_category = validated_data.pop('sub_category')
        parent = Category.objects.create(**validated_data)
        for data in sub_category:
            parent.sub_category.create(**data)
        return parent

    def update(self, instance, validated_data):
        sub_category = validated_data.pop('sub_category')
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        for data in sub_category:
            if sub := instance.sub_category.filter(id=data.get('id')).first():
                sub.name = data.get("name")
                sub.description = data.get("description")
                sub.save()
            else:
                instance.sub_category.create(**data)
        return instance



