from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Registration(UserCreationForm):
    class Meta:

        model = User
        fields = "username", "password1", "password2"
    username = forms.CharField(widget=forms.TextInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())


class ReasonForm(forms.ModelForm):
    class Meta:
        model = Reason
        fields = "__all__"


class AmbulanceForm(forms.ModelForm):
    class Meta:
        model = Ambulance
        fields = ("Patient_Name",
                  "Patient_Age",
                  "Patient_Contact",
                  "Location",
                  "Disease"
                  )
        disease_data = Reason.objects.all()
        CHOICES = disease_data.values('reason')
        widgets = {
            # attrs= {'class': 'list-group-item'}
            'Patient_Name': forms.TextInput(),
            'Patient_Age': forms.TextInput(),
            'Patient_Contact': forms.TextInput(),
            'Location': forms.TextInput(),
            'Disease': forms.Select(choices=CHOICES),
        }


class DiseaseForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = "__all__"


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ("Patient_Name",
                  "Appointment_type",
                  "Patient_Age",
                  "Patient_Contact",
                  "Location",
                  "Reason")
