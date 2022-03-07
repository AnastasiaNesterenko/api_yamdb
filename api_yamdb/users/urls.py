from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, getjwttoken, signup

app_name = 'users'

users_router = DefaultRouter()
users_router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/auth/token/', getjwttoken, name='token'),
    path('v1/auth/signup/', signup),
    path('v1/', include(users_router.urls)),
]
