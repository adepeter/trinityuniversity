from celery import Celery
from celery.schedules import crontab

from django.conf import settings

from tuapps.cores.tasks.country import fetch_country
from tuapps.jobs.tasks import show_demo

settings.configure()

app = Celery('TrinityUniversityProject', broker='redis://')
app.config_from_object('django.conf.settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, debug_task.s(), name='call_debug')
    # sender.add_periodic_task(2, fetch_country.s(), name='fetch_country_list_every_day')
    sender.add_periodic_task(2, show_demo.s(), name='show_demo')


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
