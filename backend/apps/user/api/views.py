from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from apps.user.models import User
from apps.user.api.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id_number"

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        id_number = request.data.get("id_number")
        password = request.data.get("password")

        try:
            user = User.objects.get(id_number=id_number)
        except User.DoesNotExist:
            return Response(
                {"detail": "No active account found with the given credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        user = authenticate(request, username=user.username, password=password)

        if user is None:
            return Response(
                {"detail": "No active account found with the given credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)

        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })

class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        return Response({
            "id": user.id,
            "id_number": user.id_number,
            "first_name" : user.first_name,
            "last_name" : user.last_name,
            "email" : user.email,
            "user_type": user.user_type.name if user.user_type else None,            
        })