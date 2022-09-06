from django.shortcuts import render
from rest_framework import generics
from .permissions import IsStaffOrAdminOrReadOnly
from .serializers import ProductSerializer

class ProductListCreateView(generics.ListCreateAPIView):
  permission_classes = [IsStaffOrAdminOrReadOnly]
  serializer_class = ProductSerializer
  