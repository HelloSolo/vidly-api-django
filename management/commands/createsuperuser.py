import os

if os.getenv("CREATESUPERUSER") == 0:
    stream = os.popen(
        f"python manage.py createsuperuser --no-input --username vidly_admin --email davidalimi148@gmail.com"
    )
    output = stream.read()
    print(output)
    os.environ["CREATESUPERUSER"] = "1"
else:
    print("Admin account already exists")
