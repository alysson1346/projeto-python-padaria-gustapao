from rest_framework import generics
from .permissions import IsStaffOrAdminOrReadOnly
from rest_framework.authentication import TokenAuthentication
from .serializers import ProductSerializer
from .models import Product


class ProductListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsStaffOrAdminOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsStaffOrAdminOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
