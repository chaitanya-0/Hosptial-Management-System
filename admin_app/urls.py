from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("",views.Admin_Home,name="Admin_Home"),
    path("Add_Doctor/",views.Add_Doctor,name="Add_Doctor"),
    path("Add_Doctor_Done/",views.Add_Doctor_Done,name="Add_Doctor_Done"),
    path("Read_Doctor/",views.Read_Doctor,name="Read_Doctor"),
    path("Update_Doctor/<int:id>",views.Update_Doctor,name="Update_Doctor"),
    path("Add_Nurse/",views.Add_Nurse,name="Add_Nurse"),
    path("Add_Nurse_Done/",views.Add_Nurse_Done,name="Add_Nurse_Done"),
    path("Read_Nurse/",views.Read_Nurse,name="Read_Nurse"),
    path("Update_Nurse/<int:id>",views.Update_Nurse,name="Update_Nurse"),

    path("Add_Room_Service/",views.Add_Room_Service,name="Add_Room_Service"),
    path("Add_Room_Service_Done/",views.Add_Room_Service_Done,name="Add_Room_Service_Done"),
    path("Read_Room_Service/",views.Read_Room_Service,name="Read_Room_Service"),
    path("Update_Room_Service/<int:id>",views.Update_Room_Service,name="Update_Room_Service"),
    path("Read_Ambulance/",views.Read_Ambulance,name="Read_Ambulance"),
    path("Read_Appointment/",views.Read_Appointment,name="Read_Appointment"),
    path("Payment",views.Payment,name="Payment"),

]
