#!/bin/sh
echo "Running migrations.."
python manage.py migrate
echo "Collecting statics.."
python manage.py collectstatic --no-input
echo "Starting server.."
python manage.py runserver 0.0.0.0:9000