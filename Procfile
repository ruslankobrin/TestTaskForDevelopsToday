web: gunicorn TestTaskForDevelopsToday.wsgi
worker: python manage.py celery worker -A TestTaskForDevelopsToday --concurrency=2 --loglevel=INFO --beat -E