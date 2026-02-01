from django.db import models
from .models import Patient
#from .models import Doctor

# Create your models here.
class Register(models.Model):
    register_id = models.BigAutoField(primary_key=True)
    patient = models.OneToOneField(Patient, on_delete=models.SET_NULL, null=True)
    #doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    