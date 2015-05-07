python manage.py runserver &
python manage.py celery -A celery_rest.task worker -B
