import os

stream = os.popen(
    f"python manage.py createsuperuser --no-input --username vidly_admin --email davidalimi148@gmail.com"
)
output = stream.read()
print(output)
