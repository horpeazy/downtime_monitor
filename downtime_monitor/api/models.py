from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class APIKey(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    key = models.CharField(max_length=60, null=False)