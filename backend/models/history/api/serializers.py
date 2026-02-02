from rest_framework import serializers
from models.history.api.models import History

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = [
            'doctor',
            'register',
            'reason_consultation',
            'actual_disease',
            'physical_examination',
            'age',
            'weight',
            'height',
            'heart_rate',
            'respiratory_rate',
            'key_findings',
            'main_diagnostic',
            'differential_diagnostic',
            'requested_exams',
            'programmed_procedures',
            'interconsultation',
            'follow_up_recommendations',
            'disability',
            'follow_up_plan',
            'prescription_details',
            'send_email',
            'cause_consultation',
            'main_diagnostic_code',
            'secondary_diagnostic_code',
            'third_diagnostic_code',
            'fourth_diagnostic_code',
            'service_cost',
            'income_concept',
            'payment_value',
            'fev_number',
            'previous_diseases',
            'previous_surgeries',
            'hospitalization',
            'allergies',
            'medicines',
            'immunization',
            'gynecologic_conditions',
            'obstetric_conditions',
            'psychiatric_conditions',
            'genetic_diseases',
            'vascular_diseases'
        ]