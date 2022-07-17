from django.contrib import admin

# Register your models here.
from . models import *



admin.site.register(Ambulance)
admin.site.register(Reason)
admin.site.register(Disease)
admin.site.register(Appointment)