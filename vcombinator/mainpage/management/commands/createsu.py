from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        print("HELLOHELLOHELLOHELLOHELLO")
        # if not User.objects.filter(username="admin").exists():
        #     User.objects.create_superuser("Test1", "example@example.com", "SummerOf17")