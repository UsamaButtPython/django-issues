from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import SAFE_METHODS,BasePermission,IsAuthenticated, AllowAny,AND,OR,NOT
class IsReadyOnlyRequest(BasePermission):

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsPostRequest(BasePermission):

    def has_permission(self, request, view):
        return request.method == "POST"
    
class PublicView(APIView):
    permission_classes = [(IsPostRequest and IsAuthenticated) | (IsReadyOnlyRequest)]
    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response({'message': 'This is a public view and does not require authentication.'})
    
    def post(self, request, format=None):
        permission_classes = [(IsPostRequest and IsAuthenticated) and AllowAny]

        print(permission_classes)
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response({'message': 'This is a public view and does not require authentication.'})

    def put(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response({'message': 'This is a public view and does not require authentication.'})

    def delete(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response({'message': 'This is a public view and does not require authentication.'})
