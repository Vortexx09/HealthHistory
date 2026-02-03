import os
from django.db import models
from apps.history.api.models import History

def exam_file_path(instance, filename):
    ext = filename.split('.')[-1]
    
    # Safely navigate the relationship
    try:
        patient_id = instance.history.register.patient.user.id_number
    except AttributeError:
        patient_id = "unknown"

    # To avoid the 'Exam' not defined error, import it inside the function
    # or use the instance's model class directly
    ExamModel = instance.__class__
    
    count = 0
    if instance.history:
        count = ExamModel.objects.filter(
            history=instance.history,
            exam_type=instance.exam_type
        ).count() + 1

    return f"exams/{patient_id}/{instance.exam_type}_{count}.{ext}"

class Exam(models.Model):
    EXAM_TYPE = [
        ('laboratorio', 'Laboratorio'),
        ('imagen', 'Imagen diagnóstica'),
        ('especialista', 'Consulta especialista'),
    ]

    exam_id = models.BigAutoField(primary_key=True)
    history = models.ForeignKey(History, on_delete=models.SET_NULL, null=True)
    exam_type = models.CharField(max_length=20, choices=EXAM_TYPE)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to=exam_file_path)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'exam'

    def __str__(self):
        return f"{self.exam_type} - {self.exam_id}"