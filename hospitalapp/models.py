from django.db import models

# Create your models here.
class Appointment(models.Model):
    patientname=models.CharField(max_length=20)
    age=models.IntegerField()
    date=models.DateField(auto_now_add=True)
    COMPONENTS={('cardiology','CARDIOLOGY'),('gynocology','GYNOCOLOGY'),('orthopedic','ORTHOPEDIC'),('neurology','NEUROLOGY'),('ent','ENT')}
    departments=models.CharField(choices=COMPONENTS,max_length=20)

class Donation(models.Model):
    donername=models.CharField(max_length=20)
    age=models.IntegerField()
    COMPONENTS={('a','A+'),('b','B+'),('ab','AB'),('o','O+')}
    bloodgroup=models.CharField(choices=COMPONENTS,max_length=10)

class Administration(models.Model):
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=20)