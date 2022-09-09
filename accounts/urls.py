from accounts.views import AcccountDetailView, AccountView, UpgradeToAdminOrStaff, DesactivateAccount, CreateEmployee
from rest_framework.authtoken import views
from django.urls import path

from accounts.views import LoginAccount

urlpatterns = [
    path("login/", LoginAccount.as_view()),
    path("", AccountView.as_view()),
    path("employee/", CreateEmployee.as_view()),
    path("<pk>/", AcccountDetailView.as_view()),
    path("<pk>/update-permissions/", UpgradeToAdminOrStaff.as_view()),
    path("<pk>/management/", DesactivateAccount.as_view()),
]
