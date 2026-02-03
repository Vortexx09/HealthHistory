from django.urls import include, path
from rest_framework.routers import DefaultRouter
from apps.register.api.views import RegisterViewSet

router = DefaultRouter()
router.register(r'', RegisterViewSet, basename='register')

urlpatterns = [
    path('', include(router.urls)),
]