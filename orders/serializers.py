from datetime import datetime
from itertools import product

from accounts.models import Account
from django.shortcuts import get_object_or_404
from products.models import Product
from orders.models import Order_Products
from products.serializers import ProductSerializer
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
        fields=['first_name', 'last_name', 'cellphone']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "comment", "withdrawal_date", "is_finished", "total", "account", "products"]
        read_only_fields= ["total", "account"]

    products = OrderProductsSerializer(many=True, source="order_products_set")
    account = AccountOrderSerializer(read_only=True)
    total = serializers.SerializerMethodField()
    
    def get_total(self, obj:Order):
        products = obj.order_products_set.values()
        total = 0

        for product in products:

            product_price = get_object_or_404(Product, id = product['product_id'])
            subtotal = total + product_price.price
            total = subtotal * product['quantity']                     
      
        return total
        

    def create(self, validated_data: dict) -> Product:
        products = validated_data.pop("order_products_set")

        order:Order = Order.objects.create(**validated_data)

        for product in products:
            product_obj = get_object_or_404(Product, id=product['product'].id)
            order.products.add(product_obj, through_defaults={"quantity": product['quantity']})

        return order
