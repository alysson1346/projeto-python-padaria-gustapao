from rest_framework import generics
from .permissions import IsStaffOrAdminOrReadOnly
from rest_framework.authentication import TokenAuthentication
from .serializers import ProductSerializer
from .models import Product

# Criacao de produto por admin e listagem geral de produtos publica
class ProductListCreateView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsStaffOrAdminOrReadOnly]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Listagem de produto por id publico, update e delete por admin
class ProductDetailsView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsStaffOrAdminOrReadOnly]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
