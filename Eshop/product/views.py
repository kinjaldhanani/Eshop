from rest_framework import permissions, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from product.models import Product
from product.serializers import ProductSerializer


class HomeView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']


class ProductView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (permissions.IsAdminUser,)

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True
        return super(ProductView, self).get_serializer(*args, **kwargs)
