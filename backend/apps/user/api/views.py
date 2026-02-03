from django.shortcuts import render
from rest_framework import viewsets, permissions
from apps.user.api.models import User
from apps.user.api.serializers import UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'dni'