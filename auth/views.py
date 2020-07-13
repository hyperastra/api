from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from firebase_admin.auth import create_user
from core.models import User
from django.utils.translation import ugettext as _
from rest_framework import status
from firebase_admin import auth
from urllib.parse import parse_qs, urlparse
from django.conf import settings
from core.helpers import send_email


class SignUpView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        params = ['email', 'password', 'first_name', 'last_name']
        missed_params = [x for x in params if x not in request.data.keys()]
        data = {}
        token = None

        if missed_params:
            messages = []
            for param in missed_params:
                messages.append({'message': f'{param} is required'})
                pass

            data['code'] = 'request-params-missed'
            data['message'] = messages
            return Response(data=data,
                            status=status.HTTP_400_BAD_REQUEST)

        first_name = request.data.get('first_name')
        last_name = request.data.get('first_name')
        email = request.data.get('email')
        password = request.data.get('password')

        user = User.objects.filter(email=email)

        if user.exists():
            data['code'] = 'email-in-use'
            data['message'] = f'The email address is already in use by another account'
            return Response(data=data,
                            status=status.HTTP_403_FORBIDDEN)

        # create_user


class ResetPasswordView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email', None)
        data = {}

        if not email:
            data['code'] = 'invalid-email-address'
            data['message'] = "Please enter a valid email address"
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        users = User.objects.filter(email=email)

        if not users.exists():
            data['code'] = 'user-not-found'
            data['message'] = "We didn't found any account with this email"
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        user = users.first()

        reset_password_link = auth.generate_password_reset_link(email)
        parsed_url = urlparse(reset_password_link)
        code = parse_qs(parsed_url.query).get('oobCode')[0]
        reset_password_url = f'{settings.DEFAULT_APPLICATION_URL}/set_password?code={code}'

        send_email(
            email=email,
            template_id='d-fa3d7fadb54941878d67d37d09891304',
            data={
                'display_name': f'{user.first_name} {user.last_name}',
                'email': email,
                'reset_password_link': reset_password_url
            }
        )

class VerifyView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # email en el request.data
        # 1. Comprobar si el email viene
        # 2. Obtener el usuario de la base de datos
        # 3 Comprobar si el usuario existe
        # 4. Poner el campo verified del user a True
        # 5. Actualizar en firebase con la funcion update_user de auth la propiedad email_verified y ponerle a True
        # 6. Devolver un 200
        pass
