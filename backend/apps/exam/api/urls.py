from django.urls import include, path
from rest_framework.routers import DefaultRouter
from apps.exam.api.views import ExamViewSet

router = DefaultRouter()
router.register(r'', ExamViewSet, basename='exam')

urlpatterns = [
    path('', include(router.urls)),
]