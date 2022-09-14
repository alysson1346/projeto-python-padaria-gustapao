from django.urls import path
from orders import views

urlpatterns = [
    path("", views.OrderView.as_view(), name="base-order-url"),
    path("today/", views.OrderForTodayView.as_view(), name="today-orders-url"),
    path("filter/", views.OrderFilteredByDateView.as_view()),
    path("<pk>/", views.OrderDetailView.as_view(), name="detail-order-url"),
    path("status/<pk>/", views.OrderStatusView.as_view(), name="update-status"),
]
