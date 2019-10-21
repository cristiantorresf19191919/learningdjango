from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def created_user(self, email, name, password=None):
        if not email:
            raise ValueError('User must have a valid email address')
        email = self.normalize_email(email)
        # create a nre model object
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def createSuperUser(self,email,name,password):
        """ Create and save a new super user with given details """
        user = self.created_user(email,name,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return True


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """modelo de la base de datos para usuarios en el sistema """
    email =models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254)
    is_activate = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['name']


    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email








