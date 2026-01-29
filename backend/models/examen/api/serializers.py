from rest_framework import serializers
from .models import Examen

class ExamenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Examen
        fields = [
            'examen_id',
            'paciente',
            'doctor',
            'tipo_examen',
            'descripcion',
            'archivo',
            'fecha_creacion',
        ]
        read_only_fields = ['examen_id', 'fecha_creacion']

    def validate_archivo(self, archivo):
        allowed_types = [
            'application/pdf',
            'image/jpeg',
            'image/png'
        ]

        if archivo.content_type not in allowed_types:
            raise serializers.ValidationError(
                'Solo se permiten archivos PDF o imágenes (JPG, PNG).'
            )

        return archivo