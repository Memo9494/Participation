from django.shortcuts import render, redirect

from .forms import AttendanceForm
# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Attendance
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from cryptography.fernet import Fernet







class AttendanceListView(ListView):
    model = Attendance
    template_name = 'home.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Decrypting nombre and apellido for each Attendance object
        for attendance in context['object_list']:
            print(attendance.alumno.nombre)
            attendance.alumno.nombre = self.decrypt_name(attendance.alumno.nombre)
            attendance.alumno.apellido = self.decrypt_name(attendance.alumno.apellido)
        return context

    def decrypt_name(self, encrypted_name):
        if encrypted_name:
            secret_key = b'HCSP-XM-YJ7L4Z_1HN7_Y86v75l0UZpejRBSq_CAv8A='
            cypher_suite = Fernet(secret_key)
            decrypted_name = cypher_suite.decrypt(encrypted_name).decode('utf-8')
            return decrypted_name
        return None

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