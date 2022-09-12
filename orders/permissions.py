from rest_framework import permissions


class IsOwnerOrStaffOrAdmin(permissions.IsAuthenticated):
  def has_object_permission(self, request, view, obj):
    return request.user == obj

class IsAdminOrStaff(permissions.IsAuthenticated):
  def has_permission(self, request, view):
    return request.user.is_superuser or request.user.is_staff
