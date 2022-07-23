from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

CHOICES_APPOINT = (
    ("NC", "New Case"), ("FolU", "Follow Up"), ("OC", "Old Case")
)

class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
    username = forms.CharField(widget=forms.TextInput())
    password1 = forms.CharField(widget=forms.PasswordInput(), label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

class ProfileCreate(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["address", "contact_no", "first_name", "last_name"]

    first_name  = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    contact_no = forms.IntegerField(widget=forms.TimeInput)
    address = forms.CharField(widget=forms.Textarea({'placeholder' : 'Enter your full address'}))


class AmbulanceForm(forms.ModelForm):
    class Meta:
        model = Ambulance
        fields = ["Patient_Name",
                  "Patient_Age",
                  "Patient_Contact",
                  "Location",
                  "Disease"
                  ]
            # attrs= {'class': 'list-group-item'}
        Patient_Name = forms.TextInput()
        Patient_Age = forms.TextInput(),
        Patient_Contact = forms.TextInput(),
        Location = forms.Textarea(),
        Disease= forms.CharField(),

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["Patient_Name",
                  "Appointment_type",
                  "Patient_Age",
                  "Patient_Contact",
                  "Location",
                  "Reason",
                  ]