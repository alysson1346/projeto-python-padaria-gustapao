from rest_framework import generics
from .permissions import AdminOrStaff
from rest_framework.authentication import TokenAuthentication
from categories.models import Categories

from categories.serializers import CategoriesSerializer
# from .serializers import ProductSerializer
# from .models import Product


class CategoriestListCreateView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AdminOrStaff]
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer



class CategoriesDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
