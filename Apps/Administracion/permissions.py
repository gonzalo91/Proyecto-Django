from rest_framework.permissions import BasePermission
from django.shortcuts import redirect
from .decorators import user_has_c_c_and_is_recolector

class IsUserRecolector(BasePermission):
    

    def has_permission(self, request, view):
        has_permission = user_has_c_c_and_is_recolector(request.user)
        
        
        if not has_permission and request.user:            
            return redirect('/')

        return has_permission