from django.db import transaction
from apps.user.models import User
from apps.patient.models import Patient
from apps.register.models import Register

def create_patient(user_data, patient_data, register_data, doctor):
    with transaction.atomic():
        user = User.objects.create_user(**user_data)
        patient = Patient.objects.create(user=user, **patient_data)
        register = Register.objects.create(
            patient=patient, 
            doctor=doctor, 
            **register_data
        )

        return user, patient, register
    