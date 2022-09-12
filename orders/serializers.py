from datetime import datetime

from accounts.models import Account
from django.shortcuts import get_object_or_404
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework import serializers

from orders.models import Order_Products

from .models import Order


class OrderProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Products
        fields = [
            "order",
            "product",
            "quantity",
        ]
        read_only_fields = ["order"]

class AccountOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields=['first_name', 'last_name', 'cellphone']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "comment", "withdrawal_date", "is_finished", "total", "account", "products"]
        read_only_fields= ["total", "account"]

    products = OrderProductsSerializer(many=True, source="order_products_set")
    account = AccountOrderSerializer(read_only=True)
    # total = serializers.SerializerMethodField()

    def create(self, validated_data: dict) -> Product:
        products = validated_data.pop("order_products_set")

        order:Order = Order.objects.create(**validated_data)

        for product in products:
            product_obj = get_object_or_404(Product, id=product['product'].id)
            order.products.add(product_obj, through_defaults={"quantity": product['quantity']})

        return order
