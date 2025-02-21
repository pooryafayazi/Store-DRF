from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

app_name ='accounts'

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    # path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    
        # login jwt
    path("jwt/create/", views.CustomTokenObtainPairView.as_view(), name="jwt-create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt-verify"),
    
    # reset password
    path('request-reset/', views.PasswordResetRequestView.as_view(), name='request_reset'),
    path('reset-password/<str:token>/', views.PasswordResetView.as_view(), name='reset_password'),
    
]