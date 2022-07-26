from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from category.models import Category
from category.serializers import CategorySerializer


class CategoryView(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    # permission_classes = (permissions.IsAdminUser,)







