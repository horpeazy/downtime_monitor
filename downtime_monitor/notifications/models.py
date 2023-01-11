from django.db import models
from django.contrib.auth.models import User

class NotificationGroup(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    emails = models.TextField()


class Notification(models.Model):
    recipient = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    sent = models.BooleanField(default=False)
