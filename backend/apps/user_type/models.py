from django.contrib.auth.models import AbstractUser
from django.db import models

class UserType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    class Meta:
        db_table = 'user_type'

    def __str__(self):
        return self.name