# apps/users/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    # Custom fields for the user model can be added here
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',  # Unique related name
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # Unique related name
        blank=True,
    )

    def __str__(self):
        return self.username
