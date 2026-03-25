from rest_framework import serializers
from apps.user_type.models import UserType

class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = [
            "name",
            "description",
        ]