from django.shortcuts import render

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions, status
from django.utils import timezone
import pytz

# Create your views here.
class LoginView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        
        # german_tz = pytz.timezone('Europe/Berlin')

        # last_login_german_time = user.last_login.astimezone(german_tz) if user.last_login else None
        # date_joined_german_time = user.date_joined.astimezone(german_tz) if user.date_joined else None
        
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'username': user.username,
            # 'last_login': last_login_german_time,
            # 'date_joined': date_joined_german_time
        })