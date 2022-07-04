from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import get_object_or_404
from Eshop.permission import IsOwner
from cart.models import Cart, Item
from cart.serializer import CartSerializer, ItemSerializer


class CartView(ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        return serializer.save(customer=self.request.user)

    """Show only authenticate user items"""
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Cart.objects.filter(customer=self.request.user.id)

    """Give permissions only authenticate user can update and delete"""
    def get_object(self):
        cart = get_object_or_404(Cart, id=self.kwargs['pk'])
        self.check_object_permissions(self.request, cart)
        return cart


class CartItemViewSet(ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    permission_classes = [IsAuthenticated]
    #
    # def perform_create(self, serializer):
    #     return serializer.save(customer=self.request.user)
    #
    """Show only authenticate user items"""

    # def get_queryset(self):
    #     if self.request.user.is_authenticated:
    #         return Item.objects.filter(customer=self.request.user.id)

    """Give permissions only authenticate user can update and delete"""
    def get_object(self):
        cart = get_object_or_404(Item, id=self.kwargs['pk'])
        self.check_object_permissions(self.request, cart)
        return cart
