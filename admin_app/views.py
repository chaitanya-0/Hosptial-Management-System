from django.shortcuts import render,redirect
from app.models import Ambulance
from app.models import Appointment

# Create your views here.
from . forms import *
from django.contrib import messages



def Admin_Home(request):
    return render(request,"admin.html")


def Add_Doctor(request):
    if request.method=="POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"New Doctor Added.!")

            return redirect("Add_Doctor_Done")
    else:
        form = DoctorForm()
    return render(request,"doctor.html",{"form":form})


def Add_Doctor_Done(request):
    return render(request,"Add_Doctor_Done.html")


def Read_Doctor(request):
    read=Doctor.objects.all()
    return render(request,"Read_Doctor.html",{"read":read})


def Update_Doctor(request,id):
    upd=Doctor.objects.get(id=id)
    update = DoctorForm(request.POST or None,request.FILES or None,instance=upd)
    if update.is_valid():
        update.save()
        return redirect("Read_Doctor")

    return render(request,"Update_Doctor.html",{"update":update})

def Add_Nurse(request):
    if request.method=="POST":
        form = NurseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"New Nurse Added.!")

            return redirect("Add_Nurse_Done")
    else:
        form = NurseForm()
    return render(request,"Nurse.html",{"form":form})

def Add_Nurse_Done(request):
    return render(request,"Add_Nurse_Done.html")


def Read_Nurse(request):
    read=Nurse.objects.all()
    return render(request,"Read_Nurse.html",{"read":read})

def Update_Nurse(request,id):
    upd=Nurse.objects.get(id=id)
    update = NurseForm(request.POST or None,request.FILES or None,instance=upd)
    if update.is_valid():
        update.save()
        return redirect("Read_Nurse")
    return render(request,"Update_Nurse.html",{"update":update})

def Add_Room_Service(request):
    if request.method=="POST":
        form = Room_ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"New Nurse Added.!")

            return redirect("Add_Room_Service_Done")
    else:
        form = Room_ServiceForm()
    return render(request,"Room_Service.html",{"form":form})

def Add_Room_Service_Done(request):
    return render(request,"Add_Room_Service_Done.html")


def Read_Room_Service(request):
    read=Room_Service.objects.all()
    return render(request,"Read_Room_Service.html",{"read":read})


def Update_Room_Service(request,id):
    upd=Nurse.objects.get(id=id)
    update = Room_ServiceForm(request.POST or None,request.FILES or None,instance=upd)
    if update.is_valid():
        update.save()
        return redirect("Read_Room_Service")
    return render(request,"Update_RoomService.html",{"update":update})    


def Read_Ambulance(request):
    read=Ambulance.objects.all()
    return render(request,"Read_Ambulance.html",{"read":read})    


def Read_Appointment(request):
    read=Appointment.objects.all()
    return render(request,"Read_Appointment.html",{"read":read})  

def Payment(request):
    return render(request,"Payment.html")    
