from django.db import models
from .TypeIncident import TypeIncident

class IncidentCategory(models.Model):
    typeIncident = models.ForeignKey(TypeIncident, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"