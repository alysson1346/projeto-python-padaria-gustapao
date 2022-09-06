from rest_framework import serializers
from datetime import datetime
from .models import Order

class OrderSerliazer(serializers.ModelSerializer):
    withdrawal_date = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ["id", "comment", "is_finished", "total"]
        extra_kwargs = {"total": {"read_only": True}, "withdrawal_date": {"read_only": True}}


    def get_withdrawal_date(self, obj: Order) -> str:
        actual_datetime = datetime.now()
        date_time = actual_datetime.strftime("%d/%m/%Y %H:%M:%S")
        return date_time
