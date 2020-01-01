from rest_framework.permissions import BasePermission


class MyPermission(BasePermission):
    message = '傻瓜，你冇权限'
    def has_permission(self, request, view):
        # 判断用户是否有权限
        # message = '傻瓜，你冇权限'
        user_obj = request.user
        if user_obj.type == 3:
            return False
        else:
            return True
