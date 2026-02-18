from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from lumo.models import User, Blog

class Command(BaseCommand):
    help = "Deletes anonymous users and their blogs after 48 hours"

    def handle(self, *args, **options):
        expiry_limit = timezone.now() - timedelta(hours=48)
        
        # Find anonymous users older than 48 hours
        expired_guests = User.objects.filter(
            email__isnull=True, 
            created_at__lt=expiry_limit
        )
        
        count = expired_guests.count()
        expired_guests.delete() # This deletes blogs too if models.CASCADE is set
        
        self.stdout.write(f"Successfully deleted {count} expired guest sessions.")