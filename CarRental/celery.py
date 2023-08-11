import os
from celery import Celery
from CarRental import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CarRental.settings')
app = Celery('CarRental')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.update(
    timezone='Europe/Sofia'
)
