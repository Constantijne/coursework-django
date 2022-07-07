from django.urls import path
from . import views

urlpatterns = [
    path('dep', views.departments, name='dep'),
    path('doc', views.doctors, name='doc'),
    path('rooms', views.rooms, name='rooms'),
    path('diag', views.diagnosis, name='diag')
]