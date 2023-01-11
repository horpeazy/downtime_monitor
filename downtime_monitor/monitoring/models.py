from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings


class Website(models.Model):
    url = models.URLField(unique=True)
    created_time = models.DateTimeField(auto_now_add=True)
    auth_scheme = models.TextField(blank=False, null=False)

    def get_absolute_url(self):
        return reverse('monitoring:website_detail', args=[str(self.id)])
    
    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] ({self.url})"


class DowntimeLog(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE, related_name='downtimelog')
    downtime_start = models.DateTimeField(blank=True, null=True)
    downtime_end = models.DateTimeField(blank=True, null=True)
    downtime_duration = models.PositiveIntegerField(null=True, blank=True)
    http_status = models.PositiveSmallIntegerField(null=True, blank=True)
    response_time = models.PositiveIntegerField(null=True, blank=True)
    error = models.TextField(blank=True, null=True)


    def __str__(self) -> str:
        return "[{}] <{}> ({})".format(self.__class__.__name__, self.website.url) 

class Monitor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    name = models.CharField(max_length=60, null=False)

    def __str__(self) -> str:
        return super().__str__()