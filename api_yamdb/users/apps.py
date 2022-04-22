"""
Приложение users отвечает за работу с пользователем:
регистрация, авторизация.
"""
from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Регистрация приложения users."""
    name = 'users'
