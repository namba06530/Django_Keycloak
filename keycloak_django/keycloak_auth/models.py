# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class CustomUser(AbstractUser):
    user_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    surname = models.CharField(max_length=255)
    email_verified = models.BooleanField(default=False)
    birth = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    city_id = models.IntegerField(null=True, blank=True)
    country_id = models.CharField(max_length=3, null=True, blank=True)
    profile_picture_url = models.URLField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    po_box = models.CharField(max_length=255, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    province = models.CharField(max_length=255, null=True, blank=True)
    region_state = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    keycloak_id = models.CharField(max_length=255, unique=True)


class PasswordResetToken(models.Model):
    user_id = models.CharField(max_length=255)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)


class EmailVerificationToken(models.Model):
    token = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.CharField(max_length=255, unique=True)
    email = models.EmailField()
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)