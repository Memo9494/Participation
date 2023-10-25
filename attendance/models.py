from django.db import models
from django.urls import reverse
from accounts.models import CustomUser

class Attendance(models.Model):
    participation_id = models.AutoField(primary_key=True)
    alumno = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
    )
    matricula = models.CharField(max_length=10, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    valor = models.BooleanField(default=False)

    def __str__(self):
        return f'Asistencia #{self.participation_id} - {self.alumno}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
    
    def get_alumno_matricula(self):
        return self.alumno.matricula

    def save(self, *args, **kwargs):
        self.matricula = self.get_alumno_matricula()
        super().save(*args, **kwargs)



