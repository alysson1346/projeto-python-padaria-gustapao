from rest_framework import serializers

from .models import Category, Ingredient, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]

    def create(self, validated_data: dict):
        category, _ = Category.objects.get_or_create(name=validated_data['name'])
        return category


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = [ "id", "name"]

    def create(self, validated_data: dict):
        ingredient, _ = Ingredient.objects.get_or_create(name=validated_data['name'])
        return ingredient

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    ingredients = IngredientsSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "price",
            "description",
            "is_available",
            "image_file",
            "category",
            "ingredients",
        ]
        optional_fields = ["image_file", "description"]

    def create(self, validated_data: dict) -> Product:
        category_data = validated_data.pop("category")
        ingredients_data = validated_data.pop("ingredients")

        category_obj, _ = Category.objects.get_or_create(**category_data)
        product = Product.objects.create(**validated_data, category=category_obj)

        for ingredient in ingredients_data:
            ingredient_obj, _ = Ingredient.objects.get_or_create(**ingredient)
            product.ingredients.add(ingredient_obj)

        return product

    def update(self, instance: Product, validated_data: dict) -> Product:

        if validated_data.get("ingredients"):
            ingredients_data = validated_data.pop("ingredients")
            instance.ingredients.clear()

            for ingredient in ingredients_data:
                ingredient_obj, _ = Ingredient.objects.get_or_create(**ingredient)
                instance.ingredients.add(ingredient_obj)

        if validated_data.get("category"):
            category_data = validated_data.pop("category")
            category_obj, _ = Category.objects.get_or_create(**category_data)
            instance.category = category_obj

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance