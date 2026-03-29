from django.shortcuts import render
from rest_framework import viewsets, permissions
from apps.patient.models import Patient
from apps.patient.api.serializers import PatientSerializer

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'user'

    def get_queryset(self):
        queryset = Patient.objects.all()
        id_number = self.request.query_params.get('id_number')
        if id_number:
            queryset = queryset.filter(user__id_number=id_number)
        return queryset