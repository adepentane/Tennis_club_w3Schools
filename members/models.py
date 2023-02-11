from socket import fromshare
from django.db import models
from django import forms
from django.utils.dateparse import parse_datetime

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    middlename = models.CharField(max_length=255, null=True, blank=True)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateTimeField(null=True, auto_now_add=True)
    #email = models.EmailField
    
    def __str__(self):
        return f"{self.firstname} {self.middlename} {self.lastname}"
