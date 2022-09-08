from rest_framework import serializers
# from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from rest_framework.authtoken.models import Token

from .models import UserProfile, Student, Mentor, Preference


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ("created_on", "updated_on", "is_deleted", "is_active")


class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        exclude = ("created_on", "updated_on", "is_deleted", "is_active")

class PreferenceSerializer(serializers.ModelSerializer):
    candidate_addtional_profile = MentorSerializer()
    class Meta:
        model = Preference
        fields = "__all__"

"""Serializer for User Registration"""
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        write_only=True, required=True
    )
    password2 = serializers.CharField(write_only=True, required=True)
    preferences = PreferenceSerializer(many=True, read_only=True)
    
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'user_type', 'password', 'password2', 'preferences')
        extra_kwargs = {
            'password': {'write_only':True}
        }


    def create(self, validated_data):
        user = UserProfile.objects.create(
            username = validated_data['username'], email = validated_data['email'], user_type=validated_data['user_type']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


"""Serializer for generating custom auth token"""
class AuthCustomTokenSerializer(serializers.Serializer):
    email_or_username = serializers.CharField()
    password = serializers.CharField(trim_whitespace=False)

    def validate(self, attrs):
        email_or_username = attrs.get('email_or_username')
        password = attrs.get('password')
        if email_or_username and password:
            # Check if user sent email
            if self.validateEmail(email_or_username):
                user_request = get_object_or_404(
                    UserProfile,
                    email=email_or_username,
                )
                email_or_username = user_request.username

            user = authenticate(username=email_or_username, password=password)

            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise ValidationError(msg)
            else:
                msg = _('Unable to log in with provided credentials.')
                raise ValidationError(msg)
        else:
            msg = _('Must include "email or username" and "password"')
            raise ValidationError(msg)

        attrs['user'] = user
        return attrs
    
    def validateEmail(self, email):
        try:
            validate_email(email)
            return True
        except ValidationError:
            return False





class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = UserProfile
        fields = ['id','email','name','password','user_type']

        extra_kwargs =  {
            'password' :{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }
    
    def create(self, validated_data):
        """Create and return a new user"""
        user = UserProfile.objects.create_user_api(
            email =  validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password'],
            user_type=validated_data['user_type']
            )
        return user
    
    
    def update(self, instance, validated_data):
        """HANDLE updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)

# class UserDetailSerializer(serializers.ModelSerializer):
    # """Serializes Proifle Feed Item"""

    # class Meta:
        # model =  UserDetail
        # fields = "__all__"
        # extra_kwargs ={
        #     'user_profile':{'read_only':True}
        # }


