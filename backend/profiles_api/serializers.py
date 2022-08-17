from rest_framework import serializers

from rest_framework.authtoken.models import Token

from profiles_api import models

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ['id','email','name','password','user_type']

        extra_kwargs =  {
            'password' :{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }
    
    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user_api(
            email =  validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password'],
            user_type=validated_data['user_type']
            )
        return user
    
    
    def update(self, instance, validated_data):
        """HANDLE updating user account"""
        if 'passowrd' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)

class UserDetailSerializer(serializers.ModelSerializer):
    """Serializes Proifle Feed Item"""

    class Meta:
        model =  models.UserDetail
        fields = "__all__"
        extra_kwargs ={
            'user_profile':{'read_only':True}
        }

