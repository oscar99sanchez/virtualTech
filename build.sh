#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python3 manage.py shell < /libreria/admin.py
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate