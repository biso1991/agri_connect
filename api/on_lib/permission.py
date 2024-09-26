from rest_framework import permissions
from api.on_lib.models import Book_project_lib


class Has_permissionOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, views, obj):
        # Single object permissions
        if isinstance(obj, Book_project_lib):
            return obj.owner.id == request.user.id
        else:
            return False
