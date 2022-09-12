from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import Response, status
from accounts.models import Account

from orders.models import Order
from orders.permissions import IsOwnerOrStaffOrAdmin
from orders.serializers import OrderSerializer


class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    permission_classes = [IsOwnerOrStaffOrAdmin]
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(account=self.request.user)


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Order.objects.all()
  permission_classes = [IsOwnerOrStaffOrAdmin]
  serializer_class = OrderSerializer
