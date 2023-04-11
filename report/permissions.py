from rest_framework.permissions import BasePermission


class IsReporter(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.reported == request.user
