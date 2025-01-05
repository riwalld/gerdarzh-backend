#!/bin/sh

echo "Running migrations…"
python manage.py migrate

echo "Compiling messages…"
django-admin compilemessages

echo "Removing old static files and collecting static files…"
rm -rvf /app/static/*
rm -rvf /var/tmp/django_cache/*
python manage.py collectstatic --noinput

echo "Starting server…"
gunicorn geriadur_api_django.wsgi --bind 0.0.0.0:8000 --timeout 60 --access-logfile - --threads ${NTHREADS:-1} --error-logfile -
