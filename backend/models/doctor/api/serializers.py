from rest_framework import serializers
from models.doctor.api.models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['tarjeta_profesional','especializacion']