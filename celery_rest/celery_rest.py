from __future__ import absolute_import

import os
from django.conf import settings
from celery import Celery


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest_api.settings')

app = Celery('image_scrap', broker=settings.BROKER_URL)
app.conf.CELERY_TASK_SERIALIZER = 'json'

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

if __name__ == '__main__':
    app.start()


