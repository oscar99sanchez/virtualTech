#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('oscar123', 'userEmail', '123')" | python manage.py shell
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate