from django.urls import path
from products import views

urlpatterns = [
    path("", views.ProductListCreateView.as_view(), name="list-create"),
    path("<pk>", views.ProductDetailsView.as_view(), name="retrieve-update-delete"),
]
