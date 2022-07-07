
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from Eshop.permissions import IsOwner
from order.models import Order, OrderItem
from order.serializers import OrderSerializer, OrderItemSerializer


class OrderView(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        """Show only authenticate user order"""
        if self.request.user.is_authenticated:
            return Order.objects.filter(customer=self.request.user.id)


# class OrderItemView(ModelViewSet):
#     serializer_class = OrderItemSerializer
#     queryset = OrderItem.objects.all()
#     permission_classes = [IsAuthenticated]



