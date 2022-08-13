from email import message
from django.db import models

# Create your models here.
class reg_user(models.Model):
    username=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone_no=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    pass2=models.CharField(max_length=200)
class complaint_reg(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    message=models.CharField(max_length=200)
         