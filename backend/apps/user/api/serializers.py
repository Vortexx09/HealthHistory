from rest_framework import serializers
from apps.user.api.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_type','names', 'surnames', 'id_number', 'id_type', 'email', 'password', 'phone', 'dob']