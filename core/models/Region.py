from django.db import models
from .Province import Province

class Region(models.Model):
    code_region = models.CharField( max_length=50,unique=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    name = models.CharField( max_length=50)