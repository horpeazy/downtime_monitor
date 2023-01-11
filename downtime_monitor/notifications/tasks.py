from django.core.mail import send_mail
from monitoring.models import Monitor



def send_website_notification(website, notification_type):
    # retrieve the website and the notification group from the database

    monitors = Monitor.objects.filter(website=website).all()
    recipients = []
    for monitor in monitors:
        notification_list = monitor.user.notificationgroup.emails
        notification_list = notification_list.split(',')
        recipients += notification_list

    # remove possible duplicates
    recipients = list(set(recipients))

    # send the notification to the group
    send_mail('Website Downtime', f'{website.url} is {notification_type}',
              'iyamuhope.nosa647@gmail.com',recipients )
