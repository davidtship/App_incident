from django.db import models
from .School import School
from .IncidentCaterory import IncidentCaterory
from django.contrib.postgres.fields import ArrayField

type_choice =[

    ('F','Faible'),
    ('M','Moyen'),
    ('G','Grave')
]

class Incident(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    student  = models.CharField(max_length=50)
    dob_student = models.DateField(auto_now=False, auto_now_add=False)
    add_student = models.CharField(max_length=50)
    father_name = models.CharField( max_length=50)
    mather_name = models.CharField( max_length=50)
    tutor_name = models.CharField( max_length=50,blank=True,null=True)
    tel  = models.CharField(max_length=50)
    cat_incident = models.ForeignKey(IncidentCaterory,  on_delete=models.CASCADE)
    place = models.CharField(max_length=50)
    type = models.CharField(choices=type_choice, max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=True)
    date_incident = models.DateTimeField( auto_now=False, auto_now_add=False)
    narration  = models.TextField()
    picture = models.JSONField(default=list, blank=True)
    actionTaken = ArrayField(models.CharField(max_length=50), blank=True, default=list)
    


    