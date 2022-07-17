from django import forms
from . models import *


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"


class NurseForm(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = "__all__"


class Room_ServiceForm(forms.ModelForm):
    class Meta:
        model = Room_Service
        fields = "__all__"
