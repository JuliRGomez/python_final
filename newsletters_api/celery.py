import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsletters_api.settings')

app = Celery('newsletters_api')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

