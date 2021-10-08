from celery import shared_task
from django.core.cache import cache

from ..services.countries import get_countries


@shared_task(name='fetch_country_list_every_day')
def fetch_country():
    cache.set('countries_list', get_countries(), timeout=86400)

