from rest_framework import viewsets
from apps.user.models import User
from apps.user.api.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id_number"