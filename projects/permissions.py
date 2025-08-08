from rest_framework import permissions

class IsProjectOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view):
        return request.user.is_authenticated
        
        
    def has_object_permission(self,request,view,obj):
        if not request.user.is_anonymous:
            return request.user == obj.user
        
        if request.user in obj.assigned_to.all():
            return request.method in permissions.SAFE_METHODS
        
        return False
        
        
        
        