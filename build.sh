#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirement.txt

python manage.py collectstatic
python manage.py migrate
python management/commands/createsuperuser.py