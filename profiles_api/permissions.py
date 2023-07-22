from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """check user who is trying to edit the profile"""
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id
    

    