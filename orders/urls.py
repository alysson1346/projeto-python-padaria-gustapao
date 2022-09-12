from django.urls import path
from orders import views

urlpatterns = [
    path('', views.OrderView.as_view(), name='base-order-url'),
    path('<pk>', views.OrderDetailView.as_view(), name='detail-order-url')
]
