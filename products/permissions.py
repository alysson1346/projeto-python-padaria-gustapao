from rest_framework import permissions
from products.models import Product

class IsAdminOrStaffOrReadOnly(permissions.BasePermission):
  def has_permission(self, request, view):
    if request.method in permissions.SAFE_METHODS:
      return True

    return request.user.is_staff or request.user.is_superuser

class IsAdminOrStaff(permissions.BasePermission):
  def has_permission(self, request, view):
    return request.user.is_staff or request.user.is_superuser
