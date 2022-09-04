from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile only"""

    def has_object_permission(self, request, view, obj):
        """check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class IsStudentUser(permissions.BasePermission):
    """Allow User of Type Student to create Student Profile"""
    def has_permission(self, request, view):
        """ check if user is student type"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return  request.user.user_type == "STUDENT"



class IsMentorUser(permissions.BasePermission):
    """Allow User of Type Student to create Student Profile"""
    def has_permission(self, request, view):
        """ check if user is student type"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return  request.user.user_type == "COACH"



class UpdateOwnDetails(permissions.BasePermission):
    """Allows user to update their own details"""

    def has_object_permission(self, request, view, obj):
       """Check if user is trying to update their own details"""
       if request.method in permissions.SAFE_METHODS:
            return True
    
        
       return obj.user_profile.id == request.user.id


    