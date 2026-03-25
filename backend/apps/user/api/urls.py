from rest_framework.routers import DefaultRouter
from apps.user.api.views import UserViewSet
from django.urls import path, include
from .views import LoginView, MeView

router = DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path("login/", LoginView.as_view(), name="log   in"),
    path("me/", MeView.as_view(), name='me'),
    path("", include(router.urls)),

]