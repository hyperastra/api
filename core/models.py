import uuid

from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import CIEmailField
from django.db import models
from django.utils import timezone

from core.managers import UserManager


class ApiKey(models.Model):
    key = models.UUIDField(default=uuid.uuid4)
    user = models.ForeignKey(
        "core.User", on_delete=models.CASCADE, related_name="api_keys"
    )

class User(AbstractUser):
    """Custom user class"""
    email = CIEmailField(unique=True, null=True)
    firebase_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=25, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    verified = models.BooleanField(default=False)
    objects = UserManager()

    REQUIRED_FIELDS = ["email" "first_name", "last_name"]

    USERNAME_FIELD = "email"

    def __str__(self):
        return str(self.email)

    class Meta:
        ordering = ["first_name"]
        indexes = [models.Index(fields=["email"]), models.Index(fields=["firebase_id"])]

class UserSetting(models.Model):
    """Model for UserSetting"""

class UserConnectedApp(models.Model):
    """Model for UserConnectedApp"""

class UserInvitation(models.Model):
    """Model for UserInvitation"""

class Device(models.Model):
    """Model for Device"""
    device = models.CharField(max_length=255, unique=True, null=False, blank=False)
    platform = models.CharField(max_length=255, null=False, blank=False)
    accepts_notifications = models.BooleanField(default=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        "core.User",
        on_delete=models.CASCADE,
        related_name="devices",
        null=False,
        blank=False,
    )

    class Meta:
        unique_together = ("device", "user")
        permissions = (("manage_all_devices", "Manage all devices"),)

class DeviceToken(models.Model):
    """Model for DeviceToken"""
    token = models.CharField(max_length=255, unique=True, null=False, blank=False)
    device = models.OneToOneField(
        Device, on_delete=models.CASCADE, related_name="token"
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Plan(models.Model):
    """Model for Plan"""
    name = models.CharField(max_length=80)
    price = models.FloatField()
