from django.db import models
from .SchoolCategory import SchoolCategory


class School(models.Model):
    num_affect = models.CharField(max_length=50,unique=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact = models.CharField( max_length=50)
    gerant  = models.CharField(max_length=50,null =True,blank=True)
    num_gerant = models.CharField(max_length=50)
    categorie = models.ForeignKey(SchoolCategory, on_delete=models.CASCADE)


