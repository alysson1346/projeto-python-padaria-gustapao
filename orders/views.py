from rest_framework import generics
from utils.mixins import SerializerByMethodMixin
from rest_framework.views import Response, Request
from datetime import datetime
from rest_framework.validators import ValidationError

from orders.models import Order
from orders.permissions import IsAdminOrStaff, IsOwner, IsOwnerAdminOrStaff
from orders.serializers import OrderSerializer, OrderStatusSerializer
import ipdb


class OrderListAllView(SerializerByMethodMixin, generics.ListCreateAPIView):

    permission_classes = [IsAdminOrStaff]

    queryset = Order.objects.all()
    serializer_map = {
        'GET': OrderSerializer,
    }


class OrderOwnerListView(SerializerByMethodMixin, generics.ListCreateAPIView):

    permission_classes = [IsOwner]

    queryset = Order.objects.all()
    serializer_map = {
        'GET': OrderSerializer,
    }

    def list(self, request: Request, *args, **kwargs):
        queryset = self.queryset.filter(account=request.user)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class OrderCreateView(SerializerByMethodMixin, generics.ListCreateAPIView):

    queryset = Order.objects.all()
    serializer_map = {
        'POST': OrderSerializer,
    }

    def perform_create(self, serializer):
        serializer.save(account=self.request.user)


class OrderDetailView(SerializerByMethodMixin, generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsOwnerAdminOrStaff]

    queryset = Order.objects.all()
    serializer_map = {
        'GET': OrderSerializer,
        'DELETE': OrderSerializer,
        'PATCH': OrderSerializer
    }

    # def perform_destroy(self, instance):
    #     ipdb.set_trace()

    #     request_withdrawal = instance.withdrawal_date
    #     today = datetime.today()

    #     if not self.request.user.is_superuser:
    #         instance.delete()

    #     if request_withdrawal.date() < today.date() or request_withdrawal.date() == today.date():
    #         raise ValidationError("Details: orders can be placed at least one day in advance")

    #     instance.delete()


class OrderStatusView(SerializerByMethodMixin, generics.RetrieveUpdateAPIView):

    permission_classes = [IsAdminOrStaff]

    queryset = Order.objects.all()
    serializer_map = {
      'PATCH': OrderStatusSerializer
    }