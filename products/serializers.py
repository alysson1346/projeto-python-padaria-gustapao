from rest_framework import serializers

from .models import Category, Ingredient, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ["id", "name"]


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    ingredients = IngredientsSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "category",
            "price",
            "description",
            "ingredients",
            "is_available",
            "image_file",
        ]

    optional_fields = ["image_file", "description"]

    def create(self, validated_data: dict) -> Product:

        category_data = validated_data.pop("category")
        ingredients_data = validated_data.pop("ingredients")

        category_obj = Category.objects.get_or_create(**category_data)
        product = Product.objects.create(**validated_data, category=category_obj)

        for ingredient in ingredients_data:
            ingredient_obj, _ = Ingredient.objects.get_or_create(**ingredient)
            product.ingredients.add(ingredient_obj)

        return product
