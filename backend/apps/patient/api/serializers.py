from rest_framework import serializers
from apps.patient.models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['patient_id', 'user', 'address', 'gender']