from rest_framework import permissions  # type: ignore


class PostCreateOrAuthenticated(permissions.BasePermission):
    """
    The request is authenticated as a user, or is a post request.
    """

    def has_permission(self, request, view) -> bool:  # type: ignore
        return bool(
            request.method == 'POST' or request.user and request.user.is_authenticated,
        )


class OwnProfilePermission(permissions.BasePermission):
    """
    Object-level permission to only allow updating his own profile
    """

    def has_object_permission(self, request, view, obj) -> bool:  # type: ignore

        # obj here is a UserProfile instance
        return obj.user == request.user
