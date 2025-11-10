from django.db import models

class SchoolCategory(models.Model):
    code_schoolCat = models.CharField( max_length=50)
    name = models.CharField(max_length=50)