import json
import os

import firebase_admin
from django.db.models import Q
from firebase_admin import auth, credentials
from rest_framework import authentication, exceptions
from django.utils import timezone

from core.models import User


class ExelyAuthentication(authentication.BaseAuthentication):
    def get_user(self, condition=None, value=None):
        try:
            user = User.objects.get(Q(**{f"{condition}": value}))
            return user
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed("The user does not exist")


class FirebaseAuthentication(ExelyAuthentication):
    def authenticate(self, request):
        id_token = request.headers.get("AUTHORIZATION")
        decoded_token = None

        if not id_token:
            return None

        try:
            decoded_token = auth.verify_id_token(id_token.split(" ")[1])
        except Exception as e:
            pass

        if not decoded_token:
            return None
        return self.get_user(condition="email", value=decoded_token.get("email")), None


class ApiKeyAuthentication(ExelyAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get("X_API_KEY")

        if not api_key:
            return None

        return self.get_user(condition="api_keys__key", value=api_key), None
