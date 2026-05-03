from django.urls import path, include
from .. import views
from rest_framework_simplejwt.views import TokenRefreshSlidingView,TokenVerifyView
urlpatterns = [
    #registration
    path('register/',views.RegistrationApiView.as_view(),name='register'),
    #change-password
    path('change-password/',views.ChangePasswordApiView.as_view(),name='change-password'),
    #config-email
    path('send-email/',views.SendEmail.as_view(),name='send-email'),
    #jwt
    path('jwt/create',views.CustomTokenObtainPairView.as_view(), name='create'),
    path('jwt/refresh/',TokenRefreshSlidingView.as_view(),name='refresh'),
    path('jwt/verify/',TokenVerifyView.as_view(),name='verify'),
]