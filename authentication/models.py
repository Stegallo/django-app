"""Custom user model for the project.

Extends ``AbstractUser`` to allow authentication by email instead of username.
For demonstration purposes this model redefines the username, email and
password fields with shorter length limits. It also designates the email as
the ``USERNAME_FIELD`` so django‑allauth will treat it as the primary login
identifier. ``REQUIRED_FIELDS`` lists any fields that must be supplied in
addition to the email when creating a user via the CLI.
"""
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    # Use the email address as the unique identifier for authentication
    USERNAME_FIELD = 'email'
    # Require a username when creating a new user via createsuperuser
    REQUIRED_FIELDS = ['username']
