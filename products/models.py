import uuid
from django.db import models
from rest_framework.validators import ValidationError

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
    class Meta:
        ordering = ['-id']
    
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50, unique=True)
    image_file = models.ImageField(
        validators=[validate_file_size], blank=True, null=True
    )
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)

    ingredients = models.ManyToManyField("products.Ingredient", related_name="products")
    category = models.ForeignKey(
        "products.Category",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="products",
    )


class Category(models.Model):
    class Meta:
        ordering = ['-id']
    
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50)

class Ingredient(models.Model):
    class Meta:
        ordering = ['-id']
    
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50)
