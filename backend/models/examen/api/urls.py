from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ExamenViewSet

router = DefaultRouter()
router.register(r'', ExamenViewSet, basename='examen')

urlpatterns = [
    path('', include(router.urls)),
]