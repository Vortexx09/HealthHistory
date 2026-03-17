from django.contrib.auth.models import AbstractUser
from django.db import models

class UserType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    class Meta:
        db_table = 'user_type'

    def __str__(self):
        return self.name


class User(AbstractUser):
    user_type = models.ForeignKey(UserType, on_delete=models.SET_NULL, null=True, blank=True)
    id_number = models.CharField(max_length=20, unique=True)
    id_type = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'user'