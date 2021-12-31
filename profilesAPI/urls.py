from django.urls import path

from profilesAPI import views


urlpatterns = [
    path('test-view/', views.TestApiView.as_view()),
]
