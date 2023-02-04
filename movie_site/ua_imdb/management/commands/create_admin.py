import secrets
import string
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


User = get_user_model()

def generate_password(length: int):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for i in range(length))


class Command(BaseCommand):
    def handle(self, *args, **options):
        if User.objects.count() == 0:
            username = 'admin'
            email = 'admin@admin.com'
            password = generate_password(15)
            admin = User.objects.create_superuser(
                username=username, 
                email=email, 
                password=password
            )
            admin.save()
            print(f"_________________________________________________ \n"
                  f"Initial ADMIN ACCOUNT email={username}, password={password} \n"
                  f"DO CHANGE THE PASSWORD AFTER FIRST LOGIN \n"
                  f"_________________________________________________ \n")
