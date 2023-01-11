import sys
from django.utils import timezone
from .models import Website, DowntimeLog, Monitor
from notifications.tasks import send_website_notification
import requests
import time


def monitor_websites():
    websites = Website.objects.all()
    response_time = None
    response = None
    for website in websites:
        try:
            start_time = time.time()
            response = requests.get(website.url)
            response_time = time.time() - start_time
            if response.status_code != 200:
                # website is down
                try:
                    # check if there is an ongoing downtime for this website
                    ongoing_downtime = DowntimeLog.objects.get(website=website, downtime_end__isnull=True)
                    if ongoing_downtime:
                        continue
                except DowntimeLog.DoesNotExist:
                    # website has been up the entire time
                    downtime_log = DowntimeLog.objects.create(website=website, response_time=response_time,
                                                             http_status=response.status_code, downtime_start=timezone.now())
                    send_website_notification(website, 'down')
            else:
                # website is up
                try:
                    # check if there is an ongoing downtime for this website
                    ongoing_downtime = DowntimeLog.objects.get(website=website, downtime_end__isnull=True)
                    ongoing_downtime.downtime_end = timezone.now()
                    duration = ongoing_downtime.downtime_end - ongoing_downtime.downtime_start
                    duration = duration.total_seconds() // 60
                    ongoing_downtime.downtime_duration = duration
                    ongoing_downtime.save()
                    send_website_notification(website, 'up')
                except DowntimeLog.DoesNotExist as e:
                    # website has been up the entire time
                    print(sys.exc_info())
                except Exception as e:
                    print(sys.exc_info())
        except ConnectionError as e:
            print(sys.exc_info())
        except Exception as e:
            # there was an error while trying to access the website
            try:
                # check if there is an ongoing downtime for this website
                ongoing_downtime = DowntimeLog.objects.get(website=website, downtime_end__isnull=True)
                if ongoing_downtime:
                    continue          
            except DowntimeLog.DoesNotExist:
                # website has been up the entire time
                downtime_log = DowntimeLog.objects.create(website=website,downtime_start=timezone.now(), error=str(e))
                send_website_notification(website, 'down')                
