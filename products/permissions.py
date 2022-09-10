from rest_framework import permissions
from products.models import Product

class IsStaffOrAdminOrReadOnly(permissions.BasePermission):

  def has_object_permission(self, request, view, obj: Product) -> str:
    if request.method in permissions.SAFE_METHODS:
      return True

    return request.user.is_staff or request.user.is_superuser