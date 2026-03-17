from rest_framework import viewsets, permissions
from apps.exam.models import Exam
from apps.exam.api.serializers import ExamSerializer

class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [permissions.AllowAny]
    #lookup_field = 'history'