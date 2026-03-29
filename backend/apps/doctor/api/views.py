from django.shortcuts import render
from rest_framework import viewsets, permissions
from apps.doctor.models import Doctor
from apps.doctor.api.serializers import DoctorSerializer

# Create your views here.
class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'doctor_id'

    def get_queryset(self):
        queryset = Doctor.objects.all()
        user_id = self.request.query_params.get('user_id')
        if user_id:
            queryset = queryset.filter(user__id=user_id)
        return queryset