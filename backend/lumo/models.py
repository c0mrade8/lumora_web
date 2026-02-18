from django.db import models

# Create your models here.
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, null=True, blank=True)
    display_name = models.CharField(max_length=100, blank=True, null=True, default="Anonymous_User")
    is_staff = models.BooleanField(default=False)
    is_guest = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_banned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_seen_at = models.DateTimeField(null=True, blank=True)
    objects = UserManager()
    USERNAME_FIELD = "id"
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.id)
    
class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
    title = models.CharField(max_length=255)
    content = models.TextField()
    
    # Optional: help users find others feeling the same way
    mood = models.CharField(max_length=100, blank=True, null=True) 
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at'] # Newest blogs first

    def __str__(self):
        return f"{self.title} by {self.author.display_name}"
