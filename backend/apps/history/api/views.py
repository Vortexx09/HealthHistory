from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.history.models import History
from apps.history.api.serializers import HistorySerializer

# Create your views here.
class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'history_id'

    filter_backends = [filters.SearchFilter]
    search_fields = ['register__patient__user__first_name', 'register__patient__user__last_name', 'register__patient__user__id_number']

    def perform_create(self, serializer):
        doctor = self.request.user.doctor
        serializer.save(doctor=doctor)

    @action(detail=False, methods=['get'])
    def get_last(self, request):
        doctor_id = request.user.doctor
        patient_id = request.query_params.get('patient_id')

        queryset = History.objects.select_related('register__patient').filter(
            doctor=doctor_id,
            register__patient_id=patient_id
        ).order_by('-issue_date').first()

        history = self.filter_queryset(queryset)

        serializer = self.get_serializer(history)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def get_all(self, request):
        doctor = request.user.doctor
        patient_id = request.query_params.get('patient_id')

        queryset = History.objects.select_related('register__patient').filter(
            doctor=doctor,
            register__patient_id=patient_id
        )

        histories = self.filter_queryset(queryset)

        serializer = self.get_serializer(histories, many=True)
        return Response(serializer.data)
