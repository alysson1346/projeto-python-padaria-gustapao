from rest_framework import permissions


class AdminOrStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        if request.user.is_staff or request.user.is_superuser:
            return True

