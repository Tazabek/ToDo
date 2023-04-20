from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    created_at = models.DateField(auto_now_add=False, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)


    def __str__(self) -> str:
        return self.username
    
    
