from django.contrib import admin
from .models import Doctors, Diagnosis, Departments, Rooms
# Register your models here.

admin.site.register(Doctors)
admin.site.register(Diagnosis)
admin.site.register(Departments)
admin.site.register(Rooms)
