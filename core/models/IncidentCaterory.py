from django.db import models

class IncidentCaterory(models.Model):
    code_incidentCat = models.CharField( max_length=50,unique=True)
    name = models.CharField(max_length=50)