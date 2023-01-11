from django.urls import path, include
from .views import SignUpView, home_view, profile_view

app_name = "users"

urlpatterns = [
    path('',  include("django.contrib.auth.urls")),
    path('register/', SignUpView.as_view()),
    path('profile/', profile_view, name='profile_view')
]