from django.shortcuts import render
from .models import Doctors, Departments, Diagnosis, Rooms


# Create your views here.
def departments(request):
    depart = Departments.objects.order_by('department_name')
    return render(request, 'hospital/departments.html', {"depart": depart})


def doctors(request):
    docs = Doctors.objects.order_by('second_name_doctor')
    return render(request, 'hospital/doctors.html', {"docs": docs})


def rooms(request):
    room = Rooms.objects.order_by('number')
    return render(request, 'hospital/rooms.html', {"room": room})


def diagnosis(request):
    diag = Diagnosis.objects.order_by('date_finish')
    return render(request, 'hospital/diagnosis.html', {"diag": diag})
