from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from Eshop.permissions import IsOwner, IsItem
from cart.models import Cart, Item
from cart.serializers import CartSerializer, ItemSerializer


class CartView(ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    permission_classes = [IsOwner, IsAuthenticated]

    def get_queryset(self):
        """Show only authenticate user cart"""
        if self.request.user.is_authenticated:
            return Cart.objects.filter(customer=self.request.user.id)


# class CartItemViewSet(ModelViewSet):
#     serializer_class = ItemSerializer
#     queryset = Item.objects.all()
#     permission_classes = [IsAuthenticated, IsItem]

