from datetime import timedelta
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

from lumo.serializers import UserSerializer
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.permissions import IsAuthenticated
user=get_user_model()

class AnonymousSignUpView(APIView):
    authentication_classes=[]
    permission_classes=[]
    def post(self, request):
        display_name = request.data.get('display_name', 'Kind Traveler')
        new_user=user.objects.create_user(display_name=display_name, is_guest=True)
        refresh=RefreshToken.for_user(new_user)
        expires_at = new_user.created_at + timedelta(hours=48)
        
        serializer = UserSerializer(new_user)
        return Response({
            "user": serializer.data,
            "tokens": {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            "expires_at": expires_at
        }, status=status.HTTP_201_CREATED)
    
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://127.0.0.1:8000/"
    client_class = OAuth2Client


class BlogListView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    # Only allow guest users with a valid token to see the feed
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically set the author to the logged-in user
        serializer.save(author=self.request.user)