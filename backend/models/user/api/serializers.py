from rest_framework import serializers
from models.user.api.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_type','name', 'surname', 'dni', 'dni_type', 'email', 'password', 'phone']