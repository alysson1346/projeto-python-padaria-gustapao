from django.urls import path
from products import views

urlpatterns = [
    path("", views.ProductListCreateView.as_view()),
    path("<pk>", views.ProductDetailsView.as_view()),
]
