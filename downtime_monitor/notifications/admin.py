from django.contrib import admin
from .models import Notification, NotificationGroup

# Register your models here.
admin.site.register(Notification)
admin.site.register(NotificationGroup)