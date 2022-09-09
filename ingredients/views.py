
from rest_framework import generics
from .permissions import AdminOrStaff
from rest_framework.authentication import TokenAuthentication
from .models import Ingredients

from .serializers import IngredientsSerializer

class IngredientsListCreateView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AdminOrStaff]
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer


class IngredientDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer