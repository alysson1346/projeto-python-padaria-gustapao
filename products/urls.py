from django.urls import path

from products import views

urlpatterns = [
    path("", views.ProductListCreateView.as_view(), name="list-create"),
    path("<pk>/", views.ProductDetailsView.as_view(), name="retrieve-update-delete"),
    path("section/ingredients/", views.IngredientsListCreateView.as_view(), name="list-ingredients"),
    path("section/ingredients/<pk>/", views.IngredientDetailsView.as_view(), name="ingredient_detail"),
    path("categories/", views.CategoryView.as_view(), name="list-categories"),
    path("categories/<pk>/", views.CategoryDetailsView.as_view(), name="category_detail"),
]
