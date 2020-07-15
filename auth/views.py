# Create your views here.
from datetime import datetime
from urllib.parse import parse_qs, urlparse

from django.conf import settings
from firebase_admin import auth
from firebase_admin.auth import (
    create_user,
    EmailAlreadyExistsError,
    generate_email_verification_link,
    create_custom_token,
)
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from core.helpers import send_email
from core.models import User


class SignUpView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        params = ["email", "password", "first_name", "last_name"]
        missed_params = [x for x in params if x not in request.data.keys()]
        data = {}
        token = None

        if missed_params:
            messages = []
            for param in missed_params:
                messages.append({"message": f"{param} is required"})
                pass

            data["code"] = "request-params-missed"
            data["message"] = messages
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        first_name = request.data.get("first_name")
        last_name = request.data.get("first_name")
        email = request.data.get("email")
        password = request.data.get("password")

        user = User.objects.filter(email=email)

        if user.exists():
            data["code"] = "email-in-use"
            data["message"] = f"The email address is already in use by another account"
            return Response(data=data, status=status.HTTP_403_FORBIDDEN)

        try:
            user_record = create_user(
                email=email,
                disabled=False,
                password=password,
                display_name=f"{first_name} {last_name}",
                email_verified=False,
            )

            User.objects.create(
                email=email,
                is_active=True,
                first_name=first_name,
                last_name=last_name,
                verified=False,
                firebase_id=user_record.uid,
            )
        except EmailAlreadyExistsError:
            data["code"] = "account-already-exist"
            data["message"] = "The user with the provided email already exists"
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            data["code"] = "account-password-short"
            data["message"] = "The provided password is too short"
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        verification_link = generate_email_verification_link(email)
        parsed_url = urlparse(verification_link)
        code = parse_qs(parsed_url.query).get("oobCode")[0]
        confirmation_url = (
            f"{settings.DEFAULT_APPLICATION_URL}/confirmation?code={code}&token={token}"
        )

        token = create_custom_token(user_record.uid)

        send_email(
            email=email,
            template_id="d-455ea016f05e4a47bd35f93fe7d26301",
            subject="Welcome to Hyperastra! Confirm Your Email",
            data={
                "display_name": f"{first_name} {last_name}",
                "confirmation_url": confirmation_url,
            },
        )

        return Response(data={"token": token}, status=status.HTTP_200_OK)


class ResetPasswordView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email", None)
        data = {}

        if not email:
            data["code"] = "invalid-email-address"
            data["message"] = "Please enter a valid email address"
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        users = User.objects.filter(email=email)

        if not users.exists():
            data["code"] = "user-not-found"
            data["message"] = "We didn't found any account with this email"
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        user = users.first()

        reset_password_link = auth.generate_password_reset_link(email)
        parsed_url = urlparse(reset_password_link)
        code = parse_qs(parsed_url.query).get("oobCode")[0]
        reset_password_url = (
            f"{settings.DEFAULT_APPLICATION_URL}/set_password?code={code}"
        )

        send_email(
            email=email,
            template_id="d-fa3d7fadb54941878d67d37d09891304",
            data={
                "display_name": f"{user.first_name} {user.last_name}",
                "email": email,
                "reset_password_link": reset_password_url,
            },
        )


class VerifyView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email", None)
        if not email:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        users = User.objects.filter(email=email)

        data = {}
        if not users.exists():
            data["code"] = "user-not-found"
            data["messsage"] = f"User email does not exist"
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)
        user = users.first()
        user.verified = True
        user.save()
        auth.update_user(user.firebase_id, email_verified=True)
        return Response(status=status.HTTP_200_OK)


class UpdateLastLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        firebase_id = request.data.get("firebase_id", None)
        if not firebase_id:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        users = User.objects.filter(firebase_id=firebase_id)
        if not users.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        user = users.first()
        user.last_login = datetime.utcnow()
        user.save()
        return Response(status=status.HTTP_200_OK)
