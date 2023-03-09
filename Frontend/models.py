from django.db import models

class CustomerDetails(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    Email=models.CharField(max_length=100,null=True,blank=True)
    Password=models.CharField(max_length=100,null=True,blank=True)
    Confirmpassword=models.CharField(max_length=100,null=True,blank=True)
# Create your models here.
