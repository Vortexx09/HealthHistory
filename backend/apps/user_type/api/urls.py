from rest_framework.routers import DefaultRouter
from apps.user_type.api.views import UserTypeViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'', UserTypeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]