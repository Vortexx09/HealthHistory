from django.db import models
from models.doctor.api.models import Doctor
from models.user.api.models import User

class Examen(models.Model):
    TIPO_EXAMEN_CHOICES = [
        ('laboratorio', 'Laboratorio'),
        ('imagen', 'Imagen diagnóstica'),
        ('especialista', 'Consulta especialista'),
    ]

    examen_id = models.BigAutoField(primary_key=True)
    paciente = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='examenes'
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.SET_NULL,
        null=True,
        related_name='examenes'
    )
    tipo_examen = models.CharField(max_length=20, choices=TIPO_EXAMEN_CHOICES)
    descripcion = models.TextField(null=True, blank=True)
    archivo = models.FileField(upload_to='examenes/')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'examen'

    def __str__(self):
        return f"{self.tipo_examen} - {self.examen_id}"