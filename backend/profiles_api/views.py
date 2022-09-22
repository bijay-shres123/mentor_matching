from venv import create
from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.settings import api_settings
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from profiles_api import permissions
from .models import Student, Mentor, UserProfile, Preference
from .permissions import IsMentorUser, IsStudentUser
from .helpers import create_preference_for_mentor_user, create_preference_for_student_user
from rest_framework.decorators import api_view

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication Token"""
    renderer_classes =  api_settings.DEFAULT_RENDERER_CLASSES


class UserRegistrationView(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    model = UserProfile
    queryset = UserProfile.objects.all()


class CustomAuthToken(ObtainAuthToken):
     def post(self, request, *args, **kwargs):
        serializer = AuthCustomTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(
                {'token': token.key, 'email': token.user.email}
            )


class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsStudentUser)
    authentication_classes = (TokenAuthentication,)
    serializer_class = StudentSerializer
    model = Student
    def get_queryset(self):
        queryset = Student.objects.filter(user = self.request.user)
        return queryset

    def retrieve(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request):
        serializer = StudentSerializer(data = request.POST)

        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MentorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsMentorUser)
    authentication_classes = (TokenAuthentication,)
    serializer_class = MentorSerializer
    model = Mentor

    def get_queryset(self):
        queryset = Mentor.objects.filter(user = self.request.user)
        return queryset

    def create(self, request):
        serializer = MentorSerializer(data = request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def create_preferences(request):
    if request.user.user_type == "STUDENT":
        create_preference_for_student_user(request.user)
    else:
        create_preference_for_mentor_user(request.user)
    return Response({"message" : "Created..."})



class PreferenceViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    model = Preference

    def get_queryset(self):
        queryset = Preference.objects.filter(user = self.request.user)
        return queryset

    def get_serializer_class(self):
        if self.request.user.user_type == "STUDENT":
            return StudentPreferenceSerializer
        return MentorPreferenceSerializer
    
    def create(self, request):
        serializer = self.get_serializer_class( data = request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(date=serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class UserProfileViewSet(viewsets.ModelViewSet):

    """Handle creating and updating profiles"""

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (permissions.UpdateOwnProfile,)

# class UserDetailViewSet(viewsets.ModelViewSet):

    # authentication_classes = (TokenAuthentication,)
    # serializer_class = UserDetailSerializer
    # queryset = models.UserDetail.objects.all()
    # permission_classes = {
    #     permissions.UpdateOwnDetails,
    #     IsAuthenticatedOrReadOnly,
        
    # }

    # def perform_create(self, serializer):
    #     """Sets the user profile to the logged in user"""
    #     serializer.save(user_profile= self.request.user)


    
#Retrieve And Update User Profile
class ProfileRetriveUpdateView(RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
