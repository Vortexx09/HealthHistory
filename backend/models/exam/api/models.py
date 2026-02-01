from django.db import models

class Exam(models.Model):
    EXAM_TYPE = [
        ('laboratorio', 'Laboratorio'),
        ('imagen', 'Imagen diagnóstica'),
        ('especialista', 'Consulta especialista'),
    ]

    exam_id = models.BigAutoField(primary_key=True)
    exam_type = models.CharField(max_length=20, choices=EXAM_TYPE)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='exams/')
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'exam'

    def __str__(self):
        return f"{self.exam_type} - {self.exam_id}"