from accounts.models import User, Profile
from rest_framework import generics
from .serializers import RegistrationSerializer,CustomTokenObtainPairSerializer,ChangePasswordSerializer,ProfileSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import serializers
from rest_framework_simplejwt.views  import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail

User = get_user_model()

class RegistrationApiView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer
    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
             serializer.save()
             data = {
                 'email':serializer.validated_data['email']
                 }
             return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class=CustomTokenObtainPairSerializer

class ChangePasswordApiView(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = self.request.user
        return obj
    
    def put(self, request, *args, **kwargs):
        self.object=self.get_object()
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get('old_password')):
                raise Response({'old_password':['Wrong password']},status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()
            return Response({'detail':'change password successfuly'},status=status.HTTP_200_OK)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    
class ProfileApiView(generics.RetrieveUpdateAPIView):
    serializer_class= ProfileSerializer
    queryset= Profile.objects.all()

    def get_object(self):
        queryset=self.get_queryset()
        obj = get_object_or_404(queryset,user=self.request.user)
        return obj
    
class SendEmail(generics.GenericAPIView):
    def post(self,request):
        send_mail(
            'Test Send Mail',
            'welcome to django rest framework',
            'mehrab@mm.com',
            ['parsa@p.com'],
            fail_silently=False
        )

        return Response({'detail':'sent email successful'},status=status.HTTP_200_OK)