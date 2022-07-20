from django.shortcuts import render, redirect

# Create your views here.
from . forms import *


def Home(request):
    return render(request, "home.html")


def Request_Abmulance(request):
    if request.method == "POST":
        form = AmbulanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Reach_Ambulance")
            # messages.success(request,"done")
    else:
        form = AmbulanceForm()
    return render(request, "ambulance.html", {"form": form})


def SignUp(request):
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Home")

    else:
        form = Registration()
    return render(request, "registration.html", {"form": form})


def Reach_Ambulance(request):
    return render(request, "Reach_Ambulance.html")


def Appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request,f'Ambulance will arrive soon.')
            return redirect("Appointment_Confirm")

    else:
        form = AppointmentForm()
    return render(request, "appointment.html", {"form": form})


def Appointment_Confirm(request):
    return render(request, "Appointment_confirm.html")