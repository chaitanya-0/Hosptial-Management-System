from django.db import models

# Create your models here.


class Reason(models.Model):
    reason = models.CharField(max_length=100)

    def __str__(self):
        return self.reason


class Ambulance(models.Model):
    Patient_Name = models.CharField(max_length=30)
    Patient_Age = models.IntegerField()
    Patient_Contact = models.IntegerField()
    Location = models.CharField(max_length=20)
    Disease = models.ForeignKey(Reason, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Patient_Name


class Disease(models.Model):
    reason = models.CharField(max_length=20)

    def __str__(self):
        return self.reason


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

    def __str__(self):
        return self.Patient_Name
