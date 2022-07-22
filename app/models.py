from django.conf import settings
from django.db import models
# Create your models here.

class Ambulance(models.Model):
    Patient_Name = models.CharField(max_length=30)
    Patient_Age = models.IntegerField()
    Patient_Contact = models.IntegerField()
    Location = models.CharField(max_length=20)
    Disease = models.CharField(max_length=200)
    date_time = models.DateTimeField(auto_now_add=True)
    dispatched = models.BooleanField(default=False)

    def __str__(self):
        return self.Patient_Name

class UserProfile(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    contact_no = models.IntegerField()
    address = models.TextField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True, default=None
    )
    def __str__(self):
        return self.first_name


class Appointment(models.Model):
    CHOICES_APPOINT = (
        ("NC", "New Case"), ("FolU", "Follow Up"), ("OC", "Old Case")
    )
    Patient_Name = models.CharField(max_length=30)
    Appointment_type = models.CharField(
        max_length=40, choices=CHOICES_APPOINT, default="NC")
    Patient_Age = models.IntegerField()
    Patient_Contact = models.IntegerField()
    Location = models.CharField(max_length=20)
    Reason = models.CharField(max_length=200)
    date_time = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)   # wether the admin assigns the patient's this appointment as seen by the doctor
    
    req_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, default=None)

    def __str__(self):
        return self.Patient_Name
