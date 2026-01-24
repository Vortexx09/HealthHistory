from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserType(models.Model):
    name = models.CharField(max_length=(50))
    description = models.CharField(max_length=(100))

    class Meta:
        db_table = 'user_type'

    def __str__(self):
        return self.name
    
class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    user_type = models.ForeignKey(UserType, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=True)
    surname = models.CharField(max_length=100, null=True)
    dni = models.CharField(max_length=20, null=True)
    dni_type = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.name