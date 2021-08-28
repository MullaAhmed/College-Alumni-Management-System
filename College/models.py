from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone


from .managers import PDEUManager


class PDEU(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(('email address'), unique=True)
    number=models.IntegerField(unique=True,verbose_name='number',null=True)
    college=models.CharField(verbose_name="college",max_length=20)
    branch=models.CharField(verbose_name="Branch",max_length=50)
    passing_year=models.IntegerField(verbose_name="passing year",null=True,default="0000")

    about_me=models.CharField(max_length=200)
    currently_working=models.CharField(max_length=200)
    previously_working=models.CharField(max_length=200)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    
    degree=models.CharField(max_length=200)
   
    
   
   


    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_PDEU =models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['number']

    objects = PDEUManager()

    def __str__(self):
        return self.email
    
    
