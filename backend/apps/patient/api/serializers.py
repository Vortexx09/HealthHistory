from rest_framework import serializers
from datetime import date
from apps.patient.models import Patient
from apps.user.api.serializers import UserSerializer

class PatientSerializer(serializers.ModelSerializer):    
    user = UserSerializer(read_only=True)
    age = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = [
            'patient_id', 
            'user', 
            'address', 
            'sex_code',
            'dob',
            'pob',
            'occupation',
            'civil_status',
            'religion',
            'age',
        ]

    def get_age(self, obj):
        if not obj.dob:
            return None
        
        today = date.today()
        return today.year - obj.dob.year - (
            (today.month, today.day) < (obj.dob.month, obj.dob.day)
        )