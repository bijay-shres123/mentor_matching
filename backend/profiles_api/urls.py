from django.urls import path, include


from profiles_api.views import ProfileRetriveUpdateView, UserLoginApiView
from rest_framework.routers import DefaultRouter
from profiles_api import views
from profiles_api.views import  (ProfileRetriveUpdateView)

router =  DefaultRouter()
router.register('profile', views.UserProfileViewSet)
router.register('userdetail', views.UserDetailViewSet)


urlpatterns = [
    path('login/', UserLoginApiView.as_view()),
    path('profile/me', ProfileRetriveUpdateView.as_view()),
    path('',include(router.urls))
]