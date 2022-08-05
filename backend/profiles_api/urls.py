from django.urls import path, include


from profiles_api.views import UserLoginApiView
from rest_framework.routers import DefaultRouter
from profiles_api import views

router =  DefaultRouter()
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('login/', UserLoginApiView.as_view()),
    path('',include(router.urls))
]