from django.urls import include, path
from rest_framework.routers import DefaultRouter
from apps.doctor.api.views import DoctorViewSet

router = DefaultRouter()
router.register(r'', DoctorViewSet, basename='doctor')

urlpatterns = [
    path('', include(router.urls)),
]