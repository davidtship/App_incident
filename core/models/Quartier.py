from django.db import models
from .Commune import Commune

class Quartier(models.Model):
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE, null=False)
    code_quartier = models.CharField( max_length=50,unique=True)
    name = models.CharField(max_length=50)
