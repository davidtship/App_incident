from django.db import models

class Province ( models.Model):
    code_province = models.CharField(max_length=50,unique=True)
    name = models.CharField(max_length=50)
