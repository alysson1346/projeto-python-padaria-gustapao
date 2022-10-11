from rest_framework import permissions
import ipdb


class IsOwner(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    ipdb.set_trace()
    return request.user.id == obj.account.id

class IsAdminOrStaff(permissions.IsAuthenticated):
  def has_permission(self, request, view):
    return request.user.is_superuser or request.user.is_staff

class IsOwnerAdminOrStaff(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    return request.user.id == obj.account.id or request.user.is_superuser or request.user.is_staff
