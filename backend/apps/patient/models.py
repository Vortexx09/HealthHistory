from django.db import models
from apps.user.models import User

# Create your models here.
class Patient(models.Model):
    patient_id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    
    address = models.CharField(max_length=100, null=True)
    sex_code = models.CharField(max_length=1, null=True)
    dob = models.DateField(null=True, blank=True)
    pob = models.CharField(max_length=100, null=True)
    occupation = models.CharField(max_length=100, null=True)
    
    civil_status = models.CharField(max_length=50, null=True)
    religion = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'patient'

    def __str__(self):
        if self.user:
            return str(self.user.id)
        return "Patient without user"