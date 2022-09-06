from dataclasses import fields

from rest_framework import serializers

from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model: Category
    fields = [
      "id",
      "name"
    ]

class ProductSerializer(serializers.ModelSerializer):
  class Meta: 
    model: Product
    fields = [
      "id",
      "image_file",
      "description",
      "price",
      "is_available",
      "ingredients",
      "has_lactoses",
      "has_gluten",
      "has_egg",
      "category",
    ]
    
    category = CategorySerializer()

