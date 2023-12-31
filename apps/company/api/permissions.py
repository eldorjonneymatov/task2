from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsReviewOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, review_obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user == review_obj.profile.user
