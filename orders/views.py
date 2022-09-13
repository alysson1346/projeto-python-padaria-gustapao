from rest_framework import generics
from utils.mixins import SerializerByMethodMixin
from rest_framework.views import Response, status
from accounts.models import Account

from orders.models import Order
from orders.permissions import IsOwnerOrStaffOrAdmin, IsAdminOrStaff
from orders.serializers import (
    OrderSerializer,
    OrderStatusSerializer,
    OrderFilterSerializer,
)
from django.shortcuts import get_list_or_404


class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    # permission_classes = [IsOwnerOrStaffOrAdmin]
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(account=self.request.user)


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    # permission_classes = [IsOwnerOrStaffOrAdmin]
    serializer_class = OrderSerializer


class OrderStatusView(SerializerByMethodMixin, generics.RetrieveUpdateAPIView):

    permission_classes = [IsAdminOrStaff]

    queryset = Order.objects.all()
    serializer_map = {"PATCH": OrderStatusSerializer}


class OrderFilterView(generics.ListAPIView):
    # permission_classes = [IsOwnerOrStaffOrAdmin]
    queryset = Order.objects.all()
    serializer_class = OrderFilterSerializer
