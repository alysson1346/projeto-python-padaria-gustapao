from django.urls import path

from products import views

urlpatterns = [
    path("", views.ProductListCreateView.as_view()),
    path("<pk>/", views.ProductDetailsView.as_view()),
    path("section/ingredients/", views.IngredientsListCreateView.as_view(), name="list-ingredients"),
    path("section/ingredients/<pk>/", views.IngredientDetailsView.as_view(), name="ingredient_detail"),
    path("section/categories/", views.CategoryView.as_view(), name="list-categories"),
    path("section/categories/<pk>/", views.CategoryDetailsView.as_view(), name="category_detail"),
]
