#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install

python manage.py collectstatic
python manage.py migrate
python management/commands/createsuperuser.py