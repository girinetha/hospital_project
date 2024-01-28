from django import forms
from .models import Appointment,Donation,Administration
# class management(forms.Form):
#     CHOICES=[('1','Dermatology'),('2','Gynacology'),('3','Cardiology'),('4','Orthopic'),('5','Neurology')]
#     lastname=forms.CharField()
#     dropdown=forms.CharField(widget=forms.Select(choices=CHOICES))

from django.core import validators

class userregistrationform(forms.Form):
    Gender=[('male','MALE'),('female','FEMALE'),('none','NOT PREFER')]
    # firstname=forms.CharField(required=False,validators=(validators.MinLengthValidator(5),validators.MaxLengthValidator(15)))
    # lastname=forms.CharField()
    # email=forms.CharField()
    # email=forms.EmailField()
    gender=forms.CharField(widget=forms.Select(choices=Gender))
    # password=forms.CharField(widget=forms.PasswordInput())
class appointmentform(forms.ModelForm):
    class Meta:
        model=Appointment
        fields='__all__'
class donationform(forms.ModelForm):
    class Meta:
        model=Donation
        fields='__all__'

class Administrationform(forms.ModelForm):
    class Meta:
        model=Administration
        fields='__all__'