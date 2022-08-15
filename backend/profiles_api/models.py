from ast import Mod
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

from django.conf import settings


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self, email, name,password:str= None, ):
        """Create a new user profile"""
        if not email:
            raise ValueError("Please provide an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using= self._db)

        return user

    def create_user_api(self, email, name,user_type,password:str= None, ):
        """Create a new user profile"""
        if not email:
            raise ValueError("Please provide an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name,user_type=user_type)

        user.set_password(password)
        user.save(using= self._db)

        return user

    def create_superuser(self, email, name,password):
        """"Create new superuser with given details"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database Model for User in the System"""
    email =  models.EmailField(max_length=255, unique=True)
    name =  models.CharField(max_length=255)

    #USER TYPE
    COACH = "COACH"
    STUDENT ="STUDENT"
    USER_TYPE_CHOICE = [
        (COACH, "Mentor"),
        (STUDENT, "Mentee"),
    ]
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICE)

    date_joined=models.DateTimeField(verbose_name="date_joined",auto_now_add=True)
    last_login=models.DateTimeField(verbose_name="last_login",auto_now=True)
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    objects =  UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email
        
    def get_full_name(self):
        """Retrive full name of user"""
        return self.name
    
    def get_short_name(self):
        """Retrive short name of user"""
        return self.name

    


class UserDetail(models.Model):
    """Take more user details"""
    user_profile =  models.ForeignKey(
         settings.AUTH_USER_MODEL,
         on_delete= models.CASCADE
     )
    #Gender Type
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"
    GENDER_TYPE_CHOICES = [
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER,"Other"),
    ]

    gender = models.CharField(max_length=20, choices=GENDER_TYPE_CHOICES)

    age = models.IntegerField()
    
    BRITISH = "BRITISH"
    ETHNICITY_TYPE_CHOICES = [
        (BRITISH, "Britis"),
        (OTHER, "Other"),
       
    ]
    ethnicity = models.CharField(max_length=20, choices=ETHNICITY_TYPE_CHOICES)
    
    ENGLISH = "ENGLISH"
    SPANISH = "SPANISH"
    LANGUAGE_TYPE_CHOICE = [
        (ENGLISH, "English"),
        (SPANISH, "Spanish"),
        (OTHER,"Other"),
    ]
    language = models.CharField(max_length=20, choices=LANGUAGE_TYPE_CHOICE)
    
    EXTROVERT = "EXTROVERT"
    INTROVERT = "INTROVERT"
    PEROSNALITY_TYPE_CHOICE = [
        (EXTROVERT, "Extrovert"),
        (INTROVERT, "Introver"),
       
    ]
    personality = models.CharField(max_length=20, choices=PEROSNALITY_TYPE_CHOICE)
    

    SCIENCE_AND_TECH = "SCIENCE_AND_TECH"
   
    FACULTY_TYPE_CHOICE = [
        (SCIENCE_AND_TECH, "Science and Technology"),
        (OTHER, "Other"),
       
    ]
    faculty = models.CharField(max_length=20, choices=FACULTY_TYPE_CHOICE)
    
    
    
    
    grade:models.CharField(max_length=255)
    
    
    discplinary_actions:models.BooleanField()

    NO_EXPERIENCE ="No Experience"
    ONE_OR_MORE = "One or More than 1 Years"
   
    TEACHING_EXPERIENCE_TYPE_CHOICE = [
        (NO_EXPERIENCE, "I don't have any experience"),
        (ONE_OR_MORE, "I have experience"),
       
    ]
    teaching_experience:models.CharField(max_length=30, choices=TEACHING_EXPERIENCE_TYPE_CHOICE)

    MENTORING_EXPERIENCE_TYPE_CHOICE = [
        (NO_EXPERIENCE, "I don't have any mentoring experience"),
        (ONE_OR_MORE, "I have mentoring experience"),
       
    ]
    mentoring_experience:models.CharField(max_length=30, choices=MENTORING_EXPERIENCE_TYPE_CHOICE)
    
    ONE_TO_FIVE_HOURS = "ONE TO FIVE HOURS"
    MORE_THAN_FIVE_HOURS = "MORE THAN FIVE HOURS"
    TIME_AVALIBILITY_TYPE_CHOICE = [
        (NO_EXPERIENCE, "I don't have any experience"),
        (ONE_OR_MORE, "I have experience"),
       
    ]
    time_availibility:models.CharField(max_length=30, choices=TIME_AVALIBILITY_TYPE_CHOICE)
    
    accept_discplinary_actions:models.BooleanField()

    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        """RETURN THE MODEL AS STRING"""
        return self.faculty