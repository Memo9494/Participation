from django.contrib import admin
from .models import Attendance

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['participation_id', 'alumno', 'fecha', 'valor']

    fields = [ 'alumno', 'valor']

admin.site.register(Attendance, AttendanceAdmin)
