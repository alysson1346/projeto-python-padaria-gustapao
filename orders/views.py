from datetime import datetime
from rest_framework import generics
from orders import serializers
from utils.mixins import SerializerByMethodMixin
from rest_framework.views import Response, Request
from datetime import datetime
from rest_framework.validators import ValidationError

from rest_framework.views import Response, Request, APIView, status
from accounts.models import Account
from orders.models import Order
from rest_framework import permissions
from orders.permissions import (
    IsAdminOrStaff,
    IsOwner,
    IsOwnerAdminOrStaff,
)
from orders.serializers import (
    OrderSerializer,
    OrderStatusSerializer,
)
from orders.permissions import IsAdminOrStaff


class OrderListAllView(SerializerByMethodMixin, generics.ListCreateAPIView):

    permission_classes = [IsAdminOrStaff]
    #serializer_class= OrderSerializer
    serializer_map = {
        'GET': OrderSerializer
    }
    queryset = Order.objects.all()


class OrderOwnerListView(SerializerByMethodMixin, generics.ListCreateAPIView):

    permission_classes = [IsOwner]
    serializer_map = {
        'GET': OrderSerializer
    }
    #serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def list(self, request: Request, *args, **kwargs):
        queryset = self.queryset.filter(account=request.user)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class OrderCreateView(SerializerByMethodMixin, generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Order.objects.all()
    serializer_map = {
        'GET': OrderSerializer,
        'POST': OrderSerializer,
    }
    # serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(account=self.request.user)


class OrderDetailView(SerializerByMethodMixin, generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsOwnerAdminOrStaff]

    queryset = Order.objects.all()
    serializer_map = {
        'GET': OrderSerializer,
        'PATCH': OrderSerializer,
    }
    #serializer_class = OrderSerializer



class OrderStatusView(SerializerByMethodMixin, generics.RetrieveUpdateAPIView):

    permission_classes = [IsAdminOrStaff]
    serializer_class = OrderStatusSerializer
    queryset = Order.objects.all()
    serializer_class = OrderStatusSerializer


class OrderForTodayView(generics.ListAPIView):
    permission_classes = [IsAdminOrStaff]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        today = datetime.today()

        order_for_today = []
        for order in queryset:
            ...
            if order.withdrawal_date.date() == today.date():
                order_for_today.append(order)

        page = self.paginate_queryset(order_for_today)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(order_for_today, many=True)
        return Response(serializer.data)


class OrderFilteredByDateView(generics.ListAPIView):
    permission_classes = [IsAdminOrStaff]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        withdrawal_date_param = request.query_params.get("withdrawal_date")

        date_to_search = datetime.strptime(withdrawal_date_param, "%Y-%m-%d")
        order_for_the_date = []

        for order in queryset:
            if order.withdrawal_date.date() == date_to_search.date():
                order_for_the_date.append(order)

        page = self.paginate_queryset(order_for_the_date)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(order_for_the_date, many=True)
        return Response(serializer.data)
