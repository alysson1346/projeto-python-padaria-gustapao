from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from .serializers import ProductSerializer
from .models import Product
from utils.mixins import SerializerByMethodMixin


from .models import Ingredient, Product, Category
from .permissions import IsAdminOrStaffOrReadOnly, IsAdminOrStaffOrReadOnly, IsAdminOrStaff
from .serializers import IngredientsSerializer, ProductSerializer, CategorySerializer


# Criacao de produto por admin e listagem geral de produtos publica
class ProductListCreateView(SerializerByMethodMixin, generics.ListCreateAPIView):
    permission_classes = [IsAdminOrStaffOrReadOnly]

    queryset = Product.objects.all()
    serializer_map = {
        'GET': ProductSerializer,
        'POST': ProductSerializer,
    }

# Listagem de produto por id publico, update e delete por admin
class ProductDetailsView(SerializerByMethodMixin ,generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrStaffOrReadOnly]

    queryset = Product.objects.all()
    serializer_map = {
        'GET': ProductSerializer,
        'PATCH': ProductSerializer,
        'DELETE': ProductSerializer
    }

#INGREDIENTS
class IngredientsListCreateView(SerializerByMethodMixin, generics.ListCreateAPIView):
    permission_classes = [IsAdminOrStaff]

    queryset = Ingredient.objects.all()
    serializer_map = {
        'GET': IngredientsSerializer,
        'POST': IngredientsSerializer,
    }

class IngredientDetailsView(SerializerByMethodMixin ,generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrStaff]

    queryset = Ingredient.objects.all()
    serializer_map = {
        'GET': IngredientsSerializer,
        'PATCH': IngredientsSerializer,
        'DELETE': IngredientsSerializer,
    }

#CATEGORY
class CategoryView(SerializerByMethodMixin ,generics.ListCreateAPIView):
    permission_classes = [IsAdminOrStaff]

    queryset = Category.objects.all()
    serializer_map = {
        'GET': CategorySerializer,
        'POST': CategorySerializer,
    }


class CategoryDetailsView(SerializerByMethodMixin ,generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_map = {
        'GET': CategorySerializer,
        'PATCH': CategorySerializer,
        'DELETE': CategorySerializer,
    }




