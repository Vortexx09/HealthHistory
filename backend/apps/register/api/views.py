from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from apps.register.models import Register
from apps.register.api.serializers import RegisterSerializer

# Create your views here.
class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer
    permissions_classes = [permissions.AllowAny]

    filter_backends = [filters.SearchFilter]
    search_fields = ['patient__user__first_name', 'patient__user__last_name', 'patient__user__id_number']

    def get_queryset(self):
        doctor = self.request.user

        return Register.objects.filter(doctor__user=doctor).select_related('patient__user')
