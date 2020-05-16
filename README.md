## Building

```bash
git clone https://github.com/ruslankobrin/TestTaskForDevelopsToday.git
python3 -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
celery worker -A TestTaskForDevelopsToday --concurrency=2 --loglevel=INFO --beat -E
```

## Heroku
https://testtaskfordevelopstoday.herokuapp.com/admin/
