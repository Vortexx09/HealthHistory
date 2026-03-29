from rest_framework import serializers
from apps.user.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "id_number",
            "id_type",
            "phone",
            "dob",
            "user_type"
        ]

    def create(self, validated_data):
        from apps.user_type.models import UserType
        from apps.patient.models import Patient

        password = validated_data.pop("password")
        validated_data["username"] = validated_data.get("email")

        # Self-registered users are always patients
        patient_type = UserType.objects.get(name='patient')
        validated_data["user_type"] = patient_type

        user = User(**validated_data)
        user.set_password(password)
        user.save()

        # Automatically create a Patient profile
        Patient.objects.create(user=user)

        return user