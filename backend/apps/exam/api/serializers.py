from rest_framework import serializers
from apps.exam.models import Exam

class ExamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exam
        fields = [
            'exam_id',
            'exam_type',
            'description',
            'file',
            'creation_date',
        ]
        
    def validate_file(self, file):
        allowed_types = [
            'application/pdf',
            'image/jpeg',
            'image/png'
        ]

        if file.content_type not in allowed_types:
            raise serializers.ValidationError(
                'Solo se permiten archivos PDF o imágenes (JPG, PNG).'
            )

        return file