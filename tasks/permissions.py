from rest_framework import permissions 

class IsTaskOwnerOrReadOnly(permissions.BasePermission):
    
    def has_permission(self,request, view):
        return request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        if request.user in obj.assigned_to.all():
            return request.method in permissions.SAFE_METHODS
        
        if obj.user == request.user:
            return True
            
        #if not request.user.is_annonymous :
            #return request.user == obj.user
        
        return False
    
        
            
        
    