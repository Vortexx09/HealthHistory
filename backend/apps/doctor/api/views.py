from django.shortcuts import render
from rest_framework import viewsets, permissions
from apps.doctor.models import Doctor
from apps.doctor.api.serializers import DoctorSerializer

# Create your views here.
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'doctor_id'