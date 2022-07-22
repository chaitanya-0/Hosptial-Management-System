from django.contrib import admin

# Register your models here.
from . models import *


admin.site.register(Ambulance)
admin.site.register(Appointment)
admin.site.register(UserProfile)