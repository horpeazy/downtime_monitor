from django.contrib import admin
from .models import DowntimeLog, Website, Monitor

# Register your models here.
admin.site.register(DowntimeLog)
admin.site.register(Website)
admin.site.register(Monitor)