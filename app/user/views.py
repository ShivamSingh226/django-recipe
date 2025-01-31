"""
Views for the user API
"""
from rest_framework import generics

from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """View to create the User View"""
    serializer_class = UserSerializer
