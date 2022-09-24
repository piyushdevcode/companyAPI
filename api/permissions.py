from rest_framework import permissions


class IsSuperAdmin(permissions.BasePermission):
    """
    Custom permission to allow access to SuperAdmin only
    """

    def has_permission(self, request, view):
        return bool(request.user.is_superuser)
