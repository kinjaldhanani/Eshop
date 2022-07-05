from rest_framework import request
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from order.models import Order, OrderItem
from order.serializer import OrderSerializer, OrderItemSerializer


class OrderView(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]

    """Show only authenticate user items"""
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Order.objects.filter(customer=self.request.user.id)

    def perform_create(self, serializer):
        return serializer.save(customer=self.request.user)


class OrderItemView(ModelViewSet):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
    permission_classes = [IsAuthenticated]

