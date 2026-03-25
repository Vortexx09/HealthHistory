from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
from apps.user.models import User
from apps.user.api.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id_number"

class LoginView(APIView):
    def post(self, request):

        id_number = request.data.get("id_number")
        password = request.data.get("password")

        user = authenticate(
            request,
            username=id_number,
            password=password
        )

        if user is None:
            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response({"message": "login ok"})

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
            "user_type" : user.user_type.name,
            
        })