from datetime import datetime

from django.shortcuts import get_object_or_404
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework import serializers

from orders.models import Order_Products

from .models import Order


class ProductIdAndNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name"]
        read_only_fields = ["name",]
        
class OrderProductsSerializer(serializers.ModelSerializer):
    product_id = ProductIdAndNameSerializer()
    class Meta:
        model = Order_Products
        fields = [
            "id",
            "product_id",
            "quantity",
            # "product",
        ]
        read_only_field = ["product_id"]
    

class AccountOrderSerializer(serializers.Serializer):
    name = serializers.CharField()
    cellphone = serializers.CharField()
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "comment", "withdrawal_date", "is_finished", "total", "account", "products"]
        read_only_fields= ["total", "account"]

    products = OrderProductsSerializer(many=True)
    # account = AccountOrderSerializer(read_only=True)
    # total = serializers.SerializerMethodField()
    
    # def get_total(self, obj:Order):
    #     products:Product = obj.products
    #     subtotal = sum([products[0]["price"]] + [-price for price in products[1:]["price"]])
    #     return subtotal

    def create(self, validated_data: dict) -> Product:
        products = validated_data.pop("products")

        import ipdb

        ipdb.set_trace()

        order:Order = Order.objects.create(**validated_data)
        
        for product in products:
            product_obj = get_object_or_404(Product, id=product['product_id']['id'])
            order.products.add(product_obj, through_defaults={"quantity": product['quantity']})

        return order
