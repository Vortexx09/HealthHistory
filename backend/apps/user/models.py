from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.user_type.models import UserType

class User(AbstractUser):
    user_type = models.ForeignKey(UserType, on_delete=models.SET_NULL, null=True, blank=True)
    id_number = models.CharField(max_length=20, unique=True)
    id_type = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'user'