from rest_framework import serializers
from datetime import datetime
from .models import Order

class OrderSerliazer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ["id", "comment", "withdrawal_date", "is_finished", "total"]
        extra_kwargs = {"total": {"read_only": True}}


