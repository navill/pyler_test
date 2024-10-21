from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        if hasattr(obj, 'user'):
            return request.user == obj.user
        return False
