from rest_framework import permissions
import ipdb


# Permissão onde somente admin pode ter acesso a todas as contas
class ReadOnlyAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
      if request.method == "GET" and request.user.is_superuser:
        return True
      if request.method =="POST":
        return True
      return False


# Permissão onde somente admin ou o própio usuario tem permissão
class UpdateAndDelete(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
      return request.user.id == obj.id or request.user.is_superuser


# Somente admin tem permissão
class OnlyAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_superuser)
