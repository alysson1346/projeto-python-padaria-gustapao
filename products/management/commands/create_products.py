from products.models import Product
from products.serializers import ProductSerializer
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

# class Command(BaseCommand):
#   help = 'Create 10 randon products'

#   def handle(self, *args, **kwargs):
#     for i in range(10):
#       Product.objects.create({
        
#       })