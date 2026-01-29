from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Doctor(models.Model):
    id_doctor = models.BigAutoField(primary_key=True)
    tarjeta_profesional = models.CharField(max_length=100, null=True)
    especializacion = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'Doctor'

    def __str__(self):
        return self.id_doctor