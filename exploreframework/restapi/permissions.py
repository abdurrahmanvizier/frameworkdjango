from rest_framework.permissions import BasePermission
from framework.models import Object

class IsOwner(BasePermission):
    """Custom permission class to allow only Object owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the bucketlist owner."""
        if isinstance(obj, Object):
            return obj.owner == request.user
        return obj.owner == request.user