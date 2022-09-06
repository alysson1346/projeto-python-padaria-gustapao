from dataclasses import fields

from rest_framework import serializers

from .models import Category, Ingredient, Product


class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model: Category
    fields = [
      "id",
      "name"
    ]
    
class IngredientsSerializer(serializers.ModelSerializer):
  class Meta:
    model: Ingredient
    fields = [
      "id",
      "name"
    ]

class ProductSerializer(serializers.ModelSerializer):
  class Meta: 
    model: Product
    fields = [
      "id",
      "category",
      "price",
      "description",
      "ingredients",
      "is_available",
      "image_file",
    ]
    
    category = CategorySerializer()
    ingredients = IngredientsSerializer(many=True)

