from django.urls import include, path
from rest_framework.routers import DefaultRouter
from apps.patient.api.views import PatientViewSet, CreatePatientView

router = DefaultRouter()
router.register(r'', PatientViewSet, basename='patient')

urlpatterns = [
    path('create/', CreatePatientView.as_view(), name='create'),
    path('', include(router.urls)),
]