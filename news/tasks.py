from TestTaskForDevelopsToday.celery import app
from news.models import Like


@app.task
def clean_all_table_like():
    Like.objects.all().delete()