import sys
from .models import NotificationGroup, Notification
from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


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
