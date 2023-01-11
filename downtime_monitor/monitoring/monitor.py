from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .tasks import monitor_websites

def start():
	scheduler = BackgroundScheduler()
	scheduler.add_job(monitor_websites, 'interval', seconds=60 * 5)
	scheduler.start()