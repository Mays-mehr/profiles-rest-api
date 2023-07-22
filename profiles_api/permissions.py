from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """check the user who is trying to edit the profile"""
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id
    

class UpdateOwnStatus(permissions.BasePermission):
    """allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """check the user who is trying to update the status the profile"""
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile.id == request.user.id   
    

    