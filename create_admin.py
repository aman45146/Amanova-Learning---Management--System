import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from accounts.models import User

username = "aman"
password = "Aman@12345"

user, created = User.objects.get_or_create(username=username)

user.set_password(password)
user.is_staff = True
user.is_superuser = True
user.save()

print("Admin user ready!")