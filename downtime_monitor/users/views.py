from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from notifications.models import NotificationGroup
from api.models import APIKey


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = '/accounts/login'
    template_name = 'registration/register.html'


def home_view(request):
    if request.user.is_authenticated:
        return redirect('monitoring:website_list')
    else:
        return render(request, 'monitoring/index.html')

def profile_view(request):
    notification_group = NotificationGroup.objects.filter(user=request.user)\
        .first()
    emails = None
    if notification_group:
        emails = notification_group.emails
        emails = emails.split(',')
    try:
        api_key = request.user.apikey.key
    except Exception:
        api_key = None
    context = {
        'emails': emails,
        'api_key': api_key
    }
    return render(request, 'users/profile.html', context)