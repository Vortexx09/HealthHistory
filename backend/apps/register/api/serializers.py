from rest_framework import serializers
from apps.register.models import Register

class RegisterSerializer(serializers.ModelSerializer):
    disability = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    occupational_risk = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    occupation = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    job = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    
    class Meta:
        model = Register
        fields = ['patient',
                  'doctor',
                  'register_id',
                  'country_code',
                  'municipality_code',
                  'territory_zone_code',
                  'disability',
                  'consecutive',
                  'country_origin_code',
                  'sex_code',
                  'address',
                  'mobile_number',
                  'civil_status',
                  'occupation',
                  'service_provider_code',
                  'attention_starting_date',
                  'authorization_number',
                  'record_code',
                  'service_group_mode',
                  'service_group',
                  'service_code',
                  'health_technology_goal',
                  'diabetes',
                  'cancer',
                  'alcohol_consumption',
                  'smoker',
                  'drug_use',
                  'job',
                  'occupational_risk',
                  ]
        