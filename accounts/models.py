from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomerManager(BaseUserManager):
    def create_user(self,email,password, **extra_fileds):
        email=self.normalize_email(email)

        user=self.model(
            email=email,
            **extra_fileds
        )
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,password, **extra_fileds):
        
        extra_fileds.setdefault("is_staff",True)
        extra_fileds.setdefault("is_superuser",True)
        
        if extra_fileds.get("is_staff") is not True:
            raise ValueError ("superuser must have is_super user fields value as true")
        
        if extra_fileds.get("is_superuser") is not True:
            raise ValueError ("superuser must have is_superuser user fields value as true")
        return self.create_user(email=email,password=password,**extra_fileds)
    

class user(AbstractUser):
    email=models.CharField(max_length=100,unique=True)
    username=models.CharField(max_length=100)
    bod=models.DateField(null=True)
    objects = CustomerManager()
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["username"]
    def __str__(self):
        return self.username