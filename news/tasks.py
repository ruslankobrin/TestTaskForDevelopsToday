from TestTaskForDevelopsToday.celery import app
from news.models import Like


@app.task
def test():
    Like.objects.all().delete()