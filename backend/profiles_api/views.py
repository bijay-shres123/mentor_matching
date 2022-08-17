from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
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

class UserDetailViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.UserDetailSerializer
    queryset = models.UserDetail.objects.all()
    permission_classes = {
        permissions.UpdateOwnDetails,
        IsAuthenticatedOrReadOnly,
        
    }

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile= self.request.user)


    
#Retrieve And Update User Profile
class ProfileRetriveUpdateView(RetrieveUpdateAPIView):
    serializer_class = serializers.UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
