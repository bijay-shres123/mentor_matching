from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from profiles_api import models
from profiles_api import serializers
from profiles_api import permissions

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication Token"""
    renderer_classes =  api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileViewSet(viewsets.ModelViewSet):

    """Handle creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
