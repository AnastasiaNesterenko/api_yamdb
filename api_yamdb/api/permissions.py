"""
Приложение api.
Реализация прав доступа для разных категорий пользователей.
"""
from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdmin(BasePermission):
    """Реализация прав доступа только для админа."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.is_admin
            or request.user.is_staff
            or request.user.is_superuser
        )


class IsAdminModeratorAuthorOrReadOnly(BasePermission):
    """
    Реализация прав доступа для админа,
    модератора, автора и неавторизованного пользователя.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.method == 'POST':
            return request.user.is_authenticated
        return (request.user.is_authenticated and (
            request.user == obj.author
            or request.user.is_moderator
            or request.user.is_admin
        ))


class IsAdminUserOrReadOnly(BasePermission):
    """
    Реализация прав доступа для админа,
    авторизированного и неавторизованного пользователей.
    """

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or (
            request.user.is_authenticated and request.user.is_admin)
