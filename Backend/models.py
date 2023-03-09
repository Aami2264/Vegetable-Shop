from django.db import models

class admindb(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Contact = models.IntegerField(null=True,blank=True)
    User = models.CharField(max_length=50,null=True,blank=True)
    Pass = models.CharField(max_length=50,null=True,blank=True)
    Image = models.ImageField(upload_to='profile/',null=True,blank=True)

class categorydb(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Description = models.CharField(max_length=150,null=True,blank=True)
    Image = models.ImageField(upload_to='profile/', null=True, blank=True)

class Productdb(models.Model):
    Category = models.CharField(max_length=50,null=True,blank=True)
    Name = models.CharField(max_length=50,null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    Description = models.CharField(max_length=50,null=True,blank=True)
    Image = models.ImageField(upload_to='profile/',null=True,blank=True)

class Contactdb(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Subject = models.CharField(max_length=100,null=True,blank=True)
    Message = models.CharField(max_length=100,null=True,blank=True)
# Create your models here.
