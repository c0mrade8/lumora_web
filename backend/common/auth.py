from rest_framework.permissions import BasePermission


class IsNotBanned(BasePermission):
    """Allow access only when the user is not banned.

    This permission assumes authentication is handled by other permissions
    (e.g. `IsAuthenticated`). It returns True for anonymous users so that
    authentication policies decide access for unauthenticated requests.
    """
    message = "User account is banned."

    def has_permission(self, request, view):
        user = getattr(request, 'user', None)
        if user is None:
            return True
        # Let other permissions (like IsAuthenticated) handle anonymous users.
        if not getattr(user, 'is_authenticated', False):
            return True
        return not getattr(user, 'is_banned', False)


__all__ = ["IsNotBanned"]