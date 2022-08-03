
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

import cart
from Eshop.permissions import IsItem
from cart.models import Item
from cart.serializers import  ItemSerializer


class CartItemView(ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    permission_classes = [IsItem,IsAuthenticated]
    #
    # def get_queryset(self):
    #     """Show only authenticate user item"""
    #     if self.request.user.is_authenticated:
    #         import pdb; pdb.set_trace()
    #         return Item.objects.all()


