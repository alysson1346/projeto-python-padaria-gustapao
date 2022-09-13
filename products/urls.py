from django.urls import path

from products import views

urlpatterns = [
    path("", views.ProductListCreateView.as_view()),
    path("<pk>/", views.ProductDetailsView.as_view()),
    path("ingredients/", views.IngredientsListCreateView.as_view(), name="list-ingredients"),
    path("ingredients/<pk>/", views.IngredientDetailsView.as_view(), name="ingredient_detail"),
    path("categories/", views.CategoryView.as_view(), name="list-categories"),
    path("categories/<pk>/", views.CategoryDetailsView.as_view(), name="category_detail"),
]
