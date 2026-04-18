from rest_framework import serializers
from apps.doctor.models import Doctor
from apps.user.api.serializers import UserSerializer

class DoctorSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(read_only=True)

    class Meta:
        model = Doctor
        fields = ['user', 'professional_card', 'specialization', 'user_data',]