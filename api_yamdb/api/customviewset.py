from django.core.exceptions import PermissionDenied


class CustomModelViewSet:
    def perform_create(self, serializer):
        # надо написать про авторизацию
        if not self.request.user.is_authenticated:
            raise PermissionDenied(
                'Для выполнения данного действия '
                'необходимо авторизироваться.'
            )
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        # проверка на администратора и модератора, кто это такие и как их получить
        if (serializer.instance.author != self.request.user
                or self.request.user.role != 'admin'
                or self.request.user.role != 'moderator'):
            raise PermissionDenied(
                'У вас недостаточно прав '
                'для выполнения данного действия.'
            )
        super().perform_update(serializer)

    def perform_destroy(self, instance):
        # проверка на администратора и модератора, кто это такие и как их получить
        if (instance.author != self.request.user
                or self.request.user.role != 'admin'
                or self.request.user.role != 'moderator'):
            raise PermissionDenied(
                'У вас недостаточно прав '
                'для выполнения данного действия.'
            )
        super().perform_destroy(instance)
