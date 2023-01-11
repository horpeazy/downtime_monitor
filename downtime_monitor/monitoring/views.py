from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Website, DowntimeLog, Monitor
import datetime
import json

def website_list(request):
    # retrieve all the websites from the database
    monitors = Monitor.objects.filter(user=request.user).all()

    # create a list of dictionaries containing website information and current status
    monitor_list = []
    for monitor in monitors:
        # check if it's there's no record yet
        downtime_log = DowntimeLog.objects.filter(website=monitor.website).first()
        if not downtime_log:
            monitor.status = 'status unknown'
            monitor_list.append(monitor)
            continue
        # check if there is a current downtime log for the website
        downtime_log = DowntimeLog.objects.filter(website=monitor.website, downtime_end__isnull=True).first()
        if downtime_log:
            # website is currently down
            monitor.status = "down"
            monitor_list.append(monitor)
        else:
            # website is currently up
            monitor_list.append(monitor)

    return render(request, 'monitoring/monitor_list.html', {'monitor_list': monitor_list})


def website_detail(request, website_id):
    # retrieve all the websites and the associated logs from the database
    website = get_object_or_404(Website, pk=website_id)
    downtime_logs = DowntimeLog.objects.filter(website=website)
    for downtime_log in downtime_logs:
        if not downtime_log.downtime_duration and not downtime_log.downtime_end:
            curr_time = datetime.datetime.now().replace(tzinfo=None)
            downtime_duration = curr_time - downtime_log.downtime_start.replace(tzinfo=None)
            downtime_duration = downtime_duration.total_seconds() // 60
            downtime_log.downtime_duration = downtime_duration 
    context = {'website': website, 'downtime_logs': downtime_logs}
    return render(request, 'monitoring/website_detail.html', context)

def create_monitor(request):
    # retrive the data
    data = json.loads(request.body)
    name = data["name"]
    url = data["url"]
    website = Website.objects.filter(url=url).first()
    if website:
        monitor = Monitor.objects.create(user=request.user ,website=website, name=name)
    else:
        website = Website.objects.create(url=url)
        monitor = Monitor.objects.create(user=request.user, website=website, name=name)
    response = {
        'name': name,
        'website_id': website.id,
        'url': url,
        'created': True
    }
    return JsonResponse(response, status=201)

