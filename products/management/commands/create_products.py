from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from products.models import Category, Ingredient, Product
from products.serializers import ProductSerializer


# class Command(BaseCommand):
#   help = 'Create 10 randon products'

#   def handle(self, *args, **kwargs):
#     ingredients = Ingredient.objects.create([{'name':get_random_string(10)},
#                                             {'name':get_random_string(10)},
#                                             {'name':get_random_string(10)}])
    
#     category = Category.objects.create({'name':get_random_string(10)})
    
#     for i in range(10):
#       serializer = ProductSerializer(data={
#         name: get_random_string(5),
#         description:get_random_string(50),
#         price:10,
#         ingredients:ingredients,
#         category:category}
#       )
