from rest_framework import serializers
from apps.patient.models import Patient
from apps.user.api.serializers import UserSerializer

class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # 👈 nest user data
    user_id = serializers.PrimaryKeyRelatedField(  # 👈 still accept user ID on POST
        queryset=Patient._default_manager.none(),
        source='user',
        write_only=True
    )

    class Meta:
        model = Patient
        fields = ['patient_id', 'user', 'user_id', 'address', 'sex_code']