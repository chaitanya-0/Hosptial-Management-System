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
            return redirect(Reach_Ambulance)
            # messages.success(request,"done")
    else:
        form = AmbulanceForm()
    return render(request, "ambulance.html", {"form": form})


def SignUp(request):
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return redirect(Home)

    else:
        form = Registration()
    return render(request, "registration.html", {"form": form})


def Reach_Ambulance(request):
    return render(request, "Reach_Ambulance.html")


def Appointment_view(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form1 = form.save(commit=False)
            form1.req_by = request.user
            form.save()
            # messages.success(request,f'Ambulance will arrive soon.')
            return redirect(Appointment_Confirm)

    else:
        form = AppointmentForm()
    return render(request, "appointment.html", {"form": form})


def Appointment_Confirm(request):
    return render(request, "Appointment_confirm.html")

def usr_profile(request):
    try:
        usr_obj = UserProfile.objects.get(user = request.user)
        if not usr_obj:
            return render(request, "user_profile.html", {"user_obj": False})
        else:
            return render(request, "user_profile.html", {"user_obj": usr_obj})
    except:
        return redirect(profile_create)

def usr_appointments(request):
    appoint_list = Appointment.objects.all()
    print(appoint_list)
    return render(request,"user_appointments.html", {"usr_appoint": appoint_list})

def profile_create(request):
    form = ProfileCreate()
    if request.method == "POST":
        form = ProfileCreate(request.POST)
        if form.is_valid():
            form1 = form.save(commit=False)
            form1.user = request.user
            form.save()
            # messages.success(request,f'Profile has been Created.')
            return redirect(usr_profile)
    #the user is expected to be already authenticated, if not this view won't be accessible through the templates
    return render(request, "Profile_Create.html", {"form": form})