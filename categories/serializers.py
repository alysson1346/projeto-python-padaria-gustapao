from rest_framework  import serializers
from categories.models import Categories


class CategoriesSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)

    def create(self, validated_data: dict):
        category, _ = Categories.objects.get_or_create(title=validated_data['title'])
        return category