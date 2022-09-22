from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

from django.conf import settings
from .choices import *


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self, email, username,password:str= None, ):
        """Create a new user profile"""
        if not email:
            raise ValueError("Please provide an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username)

        user.set_password(password)
        user.save(using= self._db)

        return user

    def create_user_api(self, email, username,user_type,password:str= None, ):
        """Create a new user profile"""
        if not email:
            raise ValueError("Please provide an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username,user_type=user_type)

        user.set_password(password)
        user.save(using= self._db)

        return user

    def create_superuser(self, email, username,password):
        """"Create new superuser with given details"""
        user = self.create_user(email, username, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database Model for User in the System"""
    email =  models.EmailField(max_length=255, unique=True)
    username =  models.CharField(max_length=255)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICE)
    date_joined=models.DateTimeField(verbose_name="date_joined",auto_now_add=True)
    last_login=models.DateTimeField(verbose_name="last_login",auto_now=True)
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    objects =  UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
        
    def get_full_name(self):
        """Retrive full name of user"""
        return self.username
    
    def get_short_name(self):
        """Retrive short name of user"""
        return self.username
    
    def preferences(self):
        return self.preference_set.all()

    


class BaseModel(models.Model):
    """Take more user details"""
    user =  models.ForeignKey(
         settings.AUTH_USER_MODEL,
         on_delete= models.CASCADE,
         unique=True,
     )
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)    
    gender = models.CharField(max_length=20, choices=GENDER_TYPE_CHOICES)
    age = models.IntegerField()    
    ethnicity = models.CharField(max_length=20, choices=ETHNICITY_TYPE_CHOICES)    
    language = models.CharField(max_length=20, choices=LANGUAGE_TYPE_CHOICE)    
    personality = models.CharField(max_length=20, choices=PEROSNALITY_TYPE_CHOICE)
    faculty = models.CharField(max_length=20, choices=FACULTY_TYPE_CHOICE)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    mentor_or_mentee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, blank=True, null=True, related_name="mentor_or_mentee")

    def __str__(self):
        """RETURN THE MODEL AS STRING"""
        return self.user.username
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Student(BaseModel):
    discplinary_actions= models.CharField(max_length=255, choices=DISCPLINARY_ACTION_CHOICES)
    grade=models.CharField(max_length=255)

    def __str__(self):
        return super().__str__()

class Mentor(BaseModel):
    # student = models.ManyToManyField(Student)
    teaching_experience = models.CharField(max_length=30, choices=TEACHING_EXPERIENCE_TYPE_CHOICE)
    mentoring_experience = models.CharField(max_length=30, choices=MENTORING_EXPERIENCE_TYPE_CHOICE)
    time_availibility=models.CharField(max_length=30, choices=TIME_AVALIBILITY_TYPE_CHOICE)
    accept_discplinary_actions=models.CharField(max_length=255, choices=ACCEPT_DISCPLINARY_ACTION_CHOICES )

    def __str__(self):
        return super().__str__()


class Preference(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="preferences")
    candidate = models.ForeignKey(UserProfile, on_delete = models.CASCADE, related_name="candidate")
    rank = models.PositiveIntegerField()

    class Meta:
        ordering = ('rank',)

    
    def __str__(self) -> str:
        return "Prf of : {user} comb. with {candidate} , Rank: {rank}".format(
            user = self.user.email,
            candidate = self.candidate.email,
            rank = self.rank
        )
    
    @property
    def candidate_addtional_profile(self):
        if self.user.user_type == "STUDENT":
            return Mentor.objects.get(user = self.candidate)
        return Student.objects.get(user = self.candidate)