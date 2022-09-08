from rest_framework import generics
from .permissions import IsStaffOrAdminOrReadOnly
from rest_framework.authentication import TokenAuthentication
from .serializers import ProductSerializer
from .models import Product


class ProductListCreateView(generics.ListCreateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsStaffOrAdminOrReadOnly]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
