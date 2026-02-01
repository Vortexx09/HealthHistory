from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import RegisterViewSet

router = DefaultRouter()
router.register(r'', RegisterViewSet, basename='register')

urlpatterns = [
    path('', include(router.urls)),
]