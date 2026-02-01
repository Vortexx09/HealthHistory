from django.db import models
from models.user.api.models import User

# Create your models here.
class Patient(models.Model):
    patient_id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    affiliation_type = models.CharField(max_length=2, null=True)
    
    class Meta:
        db_table = 'patient'

    def __str__(self):
        return self.user.user_id