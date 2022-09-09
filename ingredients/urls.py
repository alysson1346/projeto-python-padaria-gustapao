
from django.urls import path
from .views import IngredientsListCreateView, IngredientDetailsView

urlpatterns = [
    path("", IngredientsListCreateView.as_view(), name="list-ingredients"),
    path("<pk>/", IngredientDetailsView.as_view(), name="ingredient_detail"),
]