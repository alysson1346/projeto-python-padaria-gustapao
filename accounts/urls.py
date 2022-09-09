from accounts.views import AcccountDetailView, AccountView, UpgradeToAdminOrStaff, DeactivateAccountView, CreateEmployee
from rest_framework.authtoken import views
from django.urls import path

from accounts.views import LoginAccount

urlpatterns = [
    path("login/", views.obtain_auth_token, name="login"),
    path("", AccountView.as_view(), name="account-view-create"),
    path("employee/", CreateEmployee.as_view(), name="create-employee"),
    path("<pk>/", AcccountDetailView.as_view(), name="account-detail"),
    path("<pk>/update-permissions/", UpgradeToAdminOrStaff.as_view(), name="admin-update"),
    path("<pk>/management/", DesactivateAccount.as_view(), name="soft-delete"),
]

