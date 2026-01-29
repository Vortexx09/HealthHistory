from django.shortcuts import render
from rest_framework import viewsets, permissions
from models.doctor.api.models import Doctor
from models.doctor.api.serializers import DoctorSerializer

# Create your views here.
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id_doctor'