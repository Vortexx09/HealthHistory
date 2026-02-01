from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Register
from .serializers import RegisterSerializer

# Create your views here.
class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer
    permissions_classes = [permissions.AllowAny]
    lookup_field = 'patient'
