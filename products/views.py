from rest_framework import generics
from .permissions import IsStaffOrAdminOrReadOnly
from rest_framework.authentication import TokenAuthentication
from .serializers import ProductSerializer
from .models import Product
from utils.mixins import SerializerByMethodMixin


class ProductListCreateView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsStaffOrAdminOrReadOnly]

    queryset = Product.objects.all()
    serializer_map = {
        'GET': ProductSerializer,
        'POST': ProductSerializer,
    }


class ProductDetailsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsStaffOrAdminOrReadOnly]

    queryset = Product.objects.all()
    serializer_map = {
        'GET': ProductSerializer,
        'PATCH': ProductSerializer,
        'DELETE': ProductSerializer
    }
