from django.urls import path, include


from profiles_api.views import ProfileRetriveUpdateView, UserLoginApiView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .views import UserProfileViewSet, UserRegistrationView, CustomAuthToken, StudentViewSet, MentorViewSet, PreferenceViewSet, create_preferences
from profiles_api.views import  (ProfileRetriveUpdateView)

router =  DefaultRouter()
router.register('profile', UserProfileViewSet)
# router.register('userdetail', UserDetailViewSet)
router.register('signup', UserRegistrationView, basename="signup")
router.register('student', StudentViewSet, basename="student")
router.register('mentor', MentorViewSet, basename="mentor")
router.register('preferences', PreferenceViewSet, basename="preferences")

urlpatterns = [
    path('profile/me', ProfileRetriveUpdateView.as_view()),
    path('',include(router.urls)),
    path('api-token-auth', views.obtain_auth_token),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('preferencecreate', create_preferences),
]