import sys
from .models import NotificationGroup, Notification
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def send_notification(request):
    if request.method == 'POST':
        message = request.POST['message']
        subject = request.POST['subject']
        group = NotificationGroup.objects.\
            get(notification_type=request.POST['type'])
        recipients = group.emails.split(',')
        for recipient in recipients:
            try:
                notification = Notification.objects.\
                    create(recipient=recipient,subject=subject, message=message)
                send_mail('Website Downtime', message,
                        'iyamuhope.nosa647@gmail.com',recipient)
                notification.sent = True
                notification.save()
            except Exception as e:
                print(sys.exc_info())
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=405)

@csrf_exempt
def create_notification(request):
    # retrive the data
    data = json.loads(request.body)
    # clean input
    emails = data["emails"]
    emails = emails.split(',')
    cleaned_emails = []
    for email in emails:
        cleaned_emails.append(email.strip())
    cleaned_emails = ','.join(cleaned_emails)
    notification_group = NotificationGroup.objects.filter(user=request.user).first()
    if notification_group:
        emails = notification_group.emails
        emails = emails + ',' + cleaned_emails
        notification_group.emails = emails
        notification_group.save()
    else:
        notification_group = NotificationGroup.objects.create(user=request.user, emails=cleaned_emails)
    response = {
        'emails': cleaned_emails.split(','),
        'created': True
    }
    return JsonResponse(response, status=201)