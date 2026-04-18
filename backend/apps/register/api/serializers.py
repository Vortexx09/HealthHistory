from rest_framework import serializers
from apps.register.models import Register
from apps.doctor.api.serializers import DoctorSerializer
from apps.user.api.serializers import UserSerializer
from apps.patient.api.serializers import PatientSerializer


class RegisterSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only=True)
    patient = PatientSerializer(read_only=True)

    class Meta:
        model = Register
        fields = ['register_id',
                  'patient',
                  'doctor',
                  'disability',
                  'diabetes',
                  'cancer',
                  'alcohol_consumption',
                  'smoker',
                  'drug_use',
                  'occupational_risk',
                  #'country_code',
                  #'municipality_code',
                  #'territory_zone_code',
                  #'consecutive',
                  #'country_origin_code',
                  #'sex_code',
                  #'address',
                  #'mobile_number',
                  #'civil_status',
                  #'occupation',
                  #'service_provider_code',
                  #'attention_starting_date',
                  #'authorization_number',
                  #'record_code',
                  #'service_group_mode',
                  #'service_group',
                  #'service_code',
                  #'health_technology_goal',
                  #'job',
                  ]

class CreatePatientSerializer(serializers.Serializer):
    user = UserSerializer()
    patient = PatientSerializer()
    register = RegisterSerializer()
