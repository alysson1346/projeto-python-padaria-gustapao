import uuid
from rest_framework.validators import ValidationError
from django.db import models

# Create your models here.

# PRODUCTS
# CATEGORIES
# IMAGES

# 1MB
MB_MULTIPLIER = 1  # trocar o 1 pelo limite em MB
MAX_FILE_SIZE = MB_MULTIPLIER * 1024 * 1024

# Extra
def validate_file_size(file):
    if file.size > MAX_FILE_SIZE:
        raise ValidationError(f"File exceed maximum size {MB_MULTIPLIER}mb")

class Product(models.Model):
  id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
  name = models.CharField(max_length=50, unique=True)
  image_file = models.ImageField(validators=[validate_file_size])
  description = models.TextField()
  price = models.DecimalField(max_digits=8, decimal_places=2)
  is_available = models.BooleanField()
  ingredients = models.TextField()
  has_lactoses = models.BooleanField()
  has_gluten = models.BooleanField()
  has_egg = models.BooleanField()

  category = models.ForeignKey('products.Category', on_delete=models.SET_NULL, blank=True, null=True, related_name='products')
  ...
  
class Category(models.Model):
  id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
  name = models.CharField(max_length=50)
  ...

