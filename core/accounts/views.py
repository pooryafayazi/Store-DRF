from django.shortcuts import render
from django.contrib.auth import views as auth_views
from .forms import AuthenticationForm
# Create your views here.

class LoginView(auth_views.LoginView):
    template_name = "accounts/login.html"    
    form_class = AuthenticationForm
    redirect_authenticated_user = True


class LogoutView(auth_views.LogoutView):
    pass
    
from rest_framework import generics, status
from rest_framework.response import Response
from .models import User
from .serializers import PasswordResetRequestSerializer, PasswordResetSerializer, CustomTokenObtainPairSerializer
import jwt
import datetime
from django.conf import settings
from .tasks import send_reset_email
import pytz

class PasswordResetRequestView(generics.GenericAPIView):
    serializer_class = PasswordResetRequestSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']

        try:
            user = User.objects.get(email=email)
            token = self.create_reset_token(user.email)
            self.send_reset_email(user.email, token)
            return Response({"message": "Reset link sent to email."}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

    def create_reset_token(self, user_email):
        local_tz = pytz.timezone("Asia/Tehran")
        return jwt.encode({
            'email': user_email,
            'exp': datetime.datetime.now(local_tz) + datetime.timedelta(hours=48),
        }, settings.SECRET_KEY, algorithm='HS256')

    def send_reset_email(self, user_email, token):
        reset_link = f"http://127.0.0.1:8000/accounts/reset-password/{token}/"
        send_reset_email.delay(user_email, reset_link)
        """
        send_mail(
            'Password Reset Request',
            f'Click the link to reset your password: {reset_link}',
            'from@example.com',
            [user_email],
            fail_silently=False,
        )
        """

class PasswordResetView(generics.GenericAPIView):
    serializer_class = PasswordResetSerializer

    def post(self, request, token, *args, **kwargs):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(email=payload['email'])

            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            new_password = serializer.validated_data['password']
            user.set_password(new_password)
            user.save()
            return Response({"message": "Your password has been reset successfully."}, status=status.HTTP_200_OK)

        except (jwt.ExpiredSignatureError, jwt.DecodeError, User.DoesNotExist):
            return Response({"error": "Invalid or expired token."}, status=status.HTTP_400_BAD_REQUEST)



from rest_framework_simplejwt.views import TokenObtainPairView
 
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
