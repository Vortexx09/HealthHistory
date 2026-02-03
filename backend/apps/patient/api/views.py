from django.shortcuts import render
from rest_framework import viewsets, permissions
from apps.patient.api.models import Patient
from apps.patient.api.serializers import PatientSerializer

# Create your views here.
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'user'