"""
Приложение users отвечает за работу с пользователем:
регистрация, авторизация.
Реализация работы админки.
"""
from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'username', 'email',
        'first_name', 'last_name',
        'bio', 'role')
    search_fields = ('username',)
    empty_value_display = '-пусто-'


admin.site.register(User, UserAdmin)
