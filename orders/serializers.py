from datetime import datetime
from datetime import date
from rest_framework.views import Response, status
from rest_framework.validators import ValidationError

from accounts.models import Account
from django.shortcuts import get_object_or_404
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework import serializers

from orders.models import Order_Products

from .models import Order


class ProductSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        field = ['id', 'name', 'price', 'image_file']

class OrderProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Products
        fields = [
            "product",
            "quantity",
        ]

    product = ProductSimpleSerializer()

class AccountOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields=['first_name', 'last_name', 'cellphone']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id","withdrawal_date", "comment", "total", "order_status", "is_finished", "account", "products",]
        read_only_fields= ["total", "account", "order_status"]

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


    def validate_withdrawal_date(self, obj):
        request_withdrawal = obj 
        today = datetime.today()
        
        if request_withdrawal.date() < today.date() or request_withdrawal.date() == today.date():
            raise ValidationError("Details: orders can be placed at least one day in advance")            
        
        return obj


    def create(self, validated_data: dict) -> Product:
        products = validated_data.pop("order_products_set")

        order:Order = Order.objects.create(**validated_data)

        for product in products:
            product_obj = get_object_or_404(Product, id=product['product'].id)
            order.products.add(product_obj, through_defaults={"quantity": product['quantity']})

        return order

class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "order_status"]
        extra_kwargs = {"order_status": {"required": True}}
