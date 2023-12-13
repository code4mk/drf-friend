import os
from django.apps import apps
from celery import Celery

def load_celery(name, bind_beat_schedule):
  app = Celery(name)
  app.config_from_object('django.conf:settings', namespace='CELERY')
  app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])
  app.conf.broker_url = os.environ.get('CELERY_BROKER')
  app.conf.beat_schedule = bind_beat_schedule
  return app