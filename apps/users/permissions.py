from rest_framework import permissions


class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if current user is an admin
        return request.user.is_authenticated and request.user.is_admin
