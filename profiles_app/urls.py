from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_app import views


router = DefaultRouter()
router.register('viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet)
'''no need for basename as we give this a queryset'''


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
