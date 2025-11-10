from django.db import models
from .Ville import Ville

class Commune(models.Model):
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE, null=False)
    code_commune = models.CharField(max_length=50,unique=True)
    name = models.CharField(max_length=50)
