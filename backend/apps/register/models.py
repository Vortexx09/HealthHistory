from django.db import models
from apps.patient.models import Patient
from apps.doctor.models import Doctor

# Create your models here.
class Register(models.Model):
    register_id = models.BigAutoField(primary_key=True)
    patient = models.OneToOneField(Patient, on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    
    country_code = models.CharField(max_length=3, null=True)
    municipality_code = models.CharField(max_length=5, null=True)
    territory_zone_code = models.CharField(max_length=2, null=True)
    disability = models.CharField(max_length=2, null=True)
    consecutive = models.CharField(max_length=7, null=True)
    country_origin_code = models.CharField(max_length=3, null=True)
    sex_code = models.CharField(max_length=1, null=True)
    address = models.CharField(max_length=100, null=True)
    mobile_number = models.CharField(max_length=20, null=True)
    civil_status = models.CharField(max_length=50, null=True)
    occupation = models.CharField(max_length=50, null=True)
    service_provider_code = models.CharField(max_length=50, null=True)
    attention_starting_date = models.DateField(null=True)
    authorization_number = models.CharField(max_length=30, null=True)
    record_code = models.CharField(max_length=10, null=True)
    service_group_mode = models.CharField(max_length=2, null=True)
    service_group = models.CharField(max_length=2, null=True)
    service_code = models.CharField(max_length=4, null=True)
    health_technology_goal = models.CharField(max_length=2, null=True)
    diabetes = models.BooleanField(null=True)
    cancer = models.BooleanField(null=True)
    alcohol_consumption = models.BooleanField(null=True)
    smoker = models.BooleanField(null=True)
    drug_use = models.BooleanField(null=True)
    job = models.TextField(null=True)
    occupational_risk = models.TextField(null=True)

    class Meta:
        db_table = 'register'

    def __str__(self):
        return str(self.patient)