from django.shortcuts import render
from rest_framework import viewsets, permissions
from apps.history.models import History
from apps.history.api.serializers import HistorySerializer

# Create your views here.
class HistoryViewSet(viewsets.ModelViewSet):
    serializer_class = HistorySerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'history_id'

    def get_queryset(self):
        queryset = History.objects.all()
        register_id = self.request.query_params.get('register')
        if register_id:
            queryset = queryset.filter(register__register_id=register_id)
        return queryset
