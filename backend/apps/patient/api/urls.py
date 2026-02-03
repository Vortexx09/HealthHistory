from django.urls import include, path
from rest_framework.routers import DefaultRouter
from apps.patient.api.views import PatientViewSet

router = DefaultRouter()
router.register(r'', PatientViewSet, basename='patient')

urlpatterns = [
    path('', include(router.urls)),
]