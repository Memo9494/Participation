from django.shortcuts import render, redirect

from .forms import AttendanceForm
# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Attendance
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class AttendanceListView(ListView):
    model = Attendance
    template_name = 'home.html'

class AttendanceDetailView(DetailView):
    model = Attendance
    template_name = 'attendance_detail.html'
    context_object_name = 'attendance_obj'

class AttendanceCreateView(CreateView):
    model = Attendance
    template_name = 'attendance_new.html'
    fields = ['alumno','valor']
    success_url = reverse_lazy('home')
    #Guardar la imagen

class AttendanceUpdateView(UpdateView):
    model = Attendance
    template_name = 'attendance_edit.html'
    fields = ['author','fecha']

class AttendanceDeleteView(DeleteView):
    model = Attendance
    template_name = 'attendance_delete.html'
    #reverse_lazy es una funcion que espera que se ejecute la vista
    success_url = reverse_lazy('home')