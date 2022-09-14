import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    class Meta:
        ordering = ['-id']
    
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    cellphone = models.CharField(max_length=12, null=True, blank=True, unique=True)
    
    REQUIRED_FIELDS = ["first_name", "last_name"]
