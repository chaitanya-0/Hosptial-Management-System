from django.urls import path
from . import views

urlpatterns = [
    path("",views.Home,name="Home"),
    path("Request_Abmulance/",views.Request_Abmulance,name="Request_Abmulance"),
    path("Reach_Ambulance/",views.Reach_Ambulance,name="Reach_Ambulance"),
    path("appointment/",views.Appointment_view,name="appointment"),
    path("Appointment_Confirm/",views.Appointment_Confirm,name="Appointment_Confirm"),
    path("SignUp/",views.SignUp,name="SignUp"),
    path("usr_appointments/",views.usr_appointments, name="usr_appointments"),
    path("profile/",views.usr_profile, name="profile"),
    path("create-profile",views.profile_create, name="profile-create"),
]