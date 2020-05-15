from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TestTaskForDevelopsToday.settings')

app = Celery('TestTaskForDevelopsToday')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()



app.conf.CELERYBEAT_SCHEDULE = {
    "delete_table": {
        "task": "news.tasks.test",
        "schedule": crontab(hour="*/24"),
    },
    "delete_table2": {
        "task": "news.tasks.test",
        "schedule": crontab(minute="*/24"),
    }
}