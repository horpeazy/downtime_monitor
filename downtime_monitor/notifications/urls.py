from django.urls import path
from .views import send_notification

app_name = "notifications"

urlpatterns = [
    path('send/', send_notification, name='send_notification'),
]