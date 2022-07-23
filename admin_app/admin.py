from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from . models import *
# Register your models here.


class Doctor_Display(admin.ModelAdmin):
    list_display = ['Name', 'Specialist']

# class admin_display(UserAdmin):
#     # if admin_user.isadmin:
#     #     x = '(Admin)'
#     # else:
#     #     x = '(Regular User)'
#     list_display = ['Username', 'isadmin']


admin.site.register(Doctor, Doctor_Display)
admin.site.register(Speciality)

admin.site.register(Shift)

admin.site.register(Nurse)
admin.site.register(Room_Service)
admin.site.register(admin_user)
# admin.site.register(admin_user, admin_display)
