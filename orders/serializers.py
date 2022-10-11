from dataclasses import fields
from datetime import datetime
from itertools import product
from pyexpat import model
from rest_framework.validators import ValidationError
from accounts.models import Account
from django.shortcuts import get_object_or_404
from products.models import Product
from rest_framework import serializers
import ipdb

from orders.models import Order_Products

from .models import Order


class OrderProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Products
        fields = [
            "product",
            "quantity",
        ]


class AccountOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["first_name", "last_name", "cellphone"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "withdrawal_date",
            "comment",
            "total",
            "order_status",
            "is_finished",
            "account",
            "products",
        ]
        read_only_fields = ["total", "account", "order_status"]

    products = OrderProductsSerializer(many=True, source="order_products_set")
    account = AccountOrderSerializer(read_only=True)
    total = serializers.SerializerMethodField()

    def get_total(self, obj: Order):
        products = obj.order_products_set.values()
        total = 0

        for product in products:
            product_price = get_object_or_404(Product, id=product["product_id"])
            subtotal = total + product_price.price
            total = subtotal * product["quantity"]

        return total

    def validate_withdrawal_date(self, obj):
        request_withdrawal = obj
        today = datetime.today()

        if (
            request_withdrawal.date() < today.date()
            or request_withdrawal.date() == today.date()
        ):
            raise ValidationError(
                "Details: orders have to be placed at least one day in advance"
            )

        return obj

    def create(self, validated_data) -> Product:
        products = validated_data.pop("order_products_set")

        order: Order = Order.objects.create(**validated_data)

        for product in products:
            product_obj = get_object_or_404(Product, id=product["product"].id)
            order.products.add(
                product_obj, through_defaults={"quantity": product["quantity"]}
            )

        return order

    def update(self, instance: Order, validated_data: dict) -> Product:

        obj = instance.withdrawal_date
        self.validate_withdrawal_date(obj)

        if validated_data.get("order_products_set"):
            orders_data = validated_data.pop("order_products_set")
            instance.products.clear()

            for product in orders_data:
                product_obj = get_object_or_404(Product, id=product['product'].id)
                instance.products.add(product_obj, through_defaults={"quantity": product['quantity']})

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "order_status"]
        extra_kwargs = {"order_status": {"required": True}}
