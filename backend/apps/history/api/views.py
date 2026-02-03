from django.shortcuts import render
from rest_framework import viewsets, permissions
from apps.history.api.models import History
from apps.history.api.serializers import HistorySerializer

# Create your views here.
class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'history_id'
