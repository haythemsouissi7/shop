from __future__ import absolute_import, unicode_literals
from django.conf import settings
import os
from celery import Celery
from celery.decorators import task


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projet5.settings')

app = Celery('projet5')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
  print('Request: {0!r}'.format(self.request))

@app.task(name="sum_two_numbers")
def ad(x, y):
    return x + y


