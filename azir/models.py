from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

class AzirUserManager(BaseUserManager):
    def create_user(self, email, create_at, password=None):
        if not email:
            raise ValueError('users must have email address')
        
        user = self.model(
            email=self.normailize_email(email),
            create_at=create_at,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

class AzirUser(AbstractBaseUser):
    email = models.CharField(max_length=255, unique=True)
    create_at = models.DateField()

    objects = AzirUserManager()

    USERNAME_FIELD = 'email'
    
    def get_username(self):
        return self.email
