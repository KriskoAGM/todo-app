from django.db import models

from django.core.validators import MinLengthValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Profile(AbstractUser):
    USERNAME_FIELD = 'username'

    username = models.CharField(
        blank=False,
        null=False,
        max_length=10,
        validators=[MinLengthValidator(2, 'The username must be a minimum of 2 chars')],
        unique=True,
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(14)],
    )

    first_name = models.CharField(
        blank=True,
        null=True,
        max_length=30,
    )

    last_name = models.CharField(
        blank=True,
        null=True,
        max_length=30,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_profiles',
        related_query_name='user_profile',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_profiles',
        related_query_name='user_profile',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username