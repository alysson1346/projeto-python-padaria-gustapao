from rest_framework import serializers

from .models import Category, Ingredient, Product



class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = [
      "id",
      "name"
    ]
    
class IngredientsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Ingredient
    fields = [
      "id",
      "name"
    ]

class ProductSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Product
    fields = [
      "id",
      "category",
      "price",
      "description",
      "ingredients",
      "is_available",
      "image_file",
    ]

    optional_fields= ['image_file', 'description']
    
  category = CategorySerializer()
  ingredients = IngredientsSerializer(many=True)
  
  def create(self, validated_data):  
    import ipdb
    ipdb.set_trace()  
    category_serializer = validated_data.pop('category')
    ingredients_list = validated_data.pop('ingredients')
    
    category_instance,_ = Category.objects.get_or_create(**category_serializer)
    
    product: Product = Product.objects.create(**validated_data, category=category_instance)
    
    for ingredient in ingredients_list:
      instance_ingredient,_ = Ingredient.objects.get_or_create(**ingredient)
      product.ingredients.add(instance_ingredient)
      
    product.save() 
          
    return product

    
  


