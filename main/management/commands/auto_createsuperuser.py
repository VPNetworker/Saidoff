from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from decouple import config

class Command(BaseCommand):
    help = 'Create a superuser with predefined credentials from .env file'

    def handle(self, *args, **kwargs):
        # Fetch variables from .env using python-decouple's config
        username = config('DJANGO_SUPERUSER_USERNAME', default='admin')
        email = config('DJANGO_SUPERUSER_EMAIL', default='admin@example.com')
        password = config('DJANGO_SUPERUSER_PASSWORD', default='supersecurepassword')

        # Check if the superuser already exists
        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING('Superuser already exists'))
        else:
            # Create the superuser
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
