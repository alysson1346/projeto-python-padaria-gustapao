from rest_framework  import serializers
from .models import Ingredients


class IngredientsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)

    def create(self, validated_data: dict):
        ingredient, _ = Ingredients.objects.get_or_create(title=validated_data['title'])
        return ingredient