from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Speciality(models.Model):
    speciality = models.CharField(max_length=200)

    def __str__(self):
        return self.speciality


class Doctor(models.Model):
    Name = models.CharField(max_length=200)
    Age = models.IntegerField()
    Specialist = models.ForeignKey(Speciality, on_delete=models.CASCADE)


class Shift(models.Model):
    shift = models.CharField(max_length=10)

    def __str__(self):
        return self.shift


class Nurse(models.Model):
    Name = models.CharField(max_length=200)
    Age = models.IntegerField()
    Department = models.CharField(max_length=20)
    Shift = models.ForeignKey(Shift, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class Room_Service(models.Model):
    GENDER = (
        ("M", "Male"), ("F", "Female"), ("O", "Other")
        )
    Name = models.CharField(max_length=200)
    Age = models.IntegerField()
    Gender = models.CharField(choices=GENDER, max_length=20)

    def __str__(self):
        return self.Name


class admin_user(models.Model):
    user = models.ForeignKey(User, to_field="username",
                             on_delete=models.CASCADE)
    isadmin = models.BooleanField(default=False)

    def __str__(self):
        if self.isadmin:
            return 'Admin'
        else:
            return 'Regular User'
