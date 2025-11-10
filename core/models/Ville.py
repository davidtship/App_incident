from django.db import models
from .Province import Province


class Ville(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, null=False)
    code_ville = models.CharField(max_length=50,unique=True)
    name = models.CharField(max_length=50)