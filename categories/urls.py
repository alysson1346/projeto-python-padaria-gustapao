from django.urls import path
from .views import CategoriesDetailsView, CategoriestListCreateView

urlpatterns = [
    path("", CategoriestListCreateView.as_view(), name="list-categories"),
    path("<pk>/", CategoriesDetailsView.as_view(), name="category_detail"),
]
