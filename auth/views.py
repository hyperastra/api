from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from  firebase_admin.auth import create_user
from core.models import User
from django.utils.translation import ugettext as _


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


