from django.urls import path, include
from .views import SignUpView, home_view

app_name = "users"

urlpatterns = [
    path('',  include("django.contrib.auth.urls")),
    path('register/', SignUpView.as_view()),
]