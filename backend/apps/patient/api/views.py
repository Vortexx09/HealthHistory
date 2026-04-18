from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.services.patient_service import create_patient
from apps.patient.models import Patient
from apps.doctor.models import Doctor
from apps.register.models import Register
from apps.patient.api.serializers import PatientSerializer
from apps.register.api.serializers import CreatePatientSerializer

# Create your views here.
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.AllowAny]
    
class CreatePatientView(APIView):
    def post(self, request):
        serializer = CreatePatientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        doctor = Doctor.objects.get(user=request.user)

        user_data = serializer.validated_data['user']
        patient_data = serializer.validated_data['patient']
        register_data = serializer.validated_data['register']

        user, patient, register = create_patient(user_data, patient_data, register_data, doctor)

        return Response(
            {
                "user_id": user.id, 
                "patient_id": patient.patient_id,
                "register_id": register.register_id,
            },
            status=status.HTTP_201_CREATED
        )