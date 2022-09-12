from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from utils.mixins import SerializerByMethodMixin

from .models import Category, Ingredient, Product
from .permissions import (IsAdminOrStaff, IsAdminOrStaffOrReadOnly)
from .serializers import (CategorySerializer, IngredientsSerializer,
                          ProductSerializer)


# Criacao de produto por admin e listagem geral de produtos publica
class ProductListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrStaffOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Listagem de produto por id publico, update e delete por admin
class ProductDetailsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrStaffOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class IngredientsListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrStaffOrReadOnly]
    queryset = Ingredient.objects.all()
    serializer_class = IngredientsSerializer


class IngredientDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientsSerializer

class CategoryView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrStaffOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
