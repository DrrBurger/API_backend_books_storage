from rest_framework import permissions


class IsAdminOrAuthOnly(permissions.BasePermission):
    """
    Кастомный permission разрешающий:
    Просмотр и добавление записей только авторизованным пользователям или админу
    Изменение записи возможно только, если ты являешься автором записи или админ
    Удаление записи только админ
    """
    def has_permission(self, request, view):
        if request.method in ['GET', 'POST', 'HEAD', 'OPTIONS', 'PUT'] and request.user.is_authenticated:
            return True

        return bool(request.user and request.user.is_staff)

    def has_object_permission(self, request, view, obj):
        user = request.user
        if request.method in ['GET', 'POST', 'PUT', 'PATCH'] \
                and user.is_authenticated\
                and user == obj.user or user.is_staff:
            return True

        return False
