from django.urls import include, path
from rest_framework.routers import DefaultRouter
from models.history.api.views import HistoryViewSet

router = DefaultRouter()
router.register(r'', HistoryViewSet, basename='history')

urlpatterns = [
    path('', include(router.urls)),
]