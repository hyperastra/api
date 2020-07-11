from django.contrib.auth.base_user import BaseUserManager
from firebase_admin.auth import create_user, EmailAlreadyExistsError, get_user_by_email

from core import models


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """ Create and save a user with the given email, and password """
        print("Creating user on the database")
        create_api_key = extra_fields.get("create_api_key")
        extra_fields.pop("create_api_key", None)
        user = self.model(email=email, **extra_fields)

        print("Creating user on Firebase Authentication")

        try:
            user_record = create_user(email=email, password=password)
        except EmailAlreadyExistsError:
            user_record = get_user_by_email(email)

        user.firebase_id = user_record.uid
        user.save(using=self._db)

        if create_api_key:
            print("Creating user API key")
            api_key = models.ApiKey.objects.create(user=user)
            print(f"API Key: {api_key.key}")

        return user

    def create_user(self, email=None, password=None, **extra_fields):
        """ Wrapper for create user that set default values """
        extra_fields.setdefault("create_api_key", False)
        email = self.normalize_email(email)
        return self._create_user(email, password, **extra_fields)