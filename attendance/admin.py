from django.db import models
from django.urls import reverse

# Create your models here.
class Attendance(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    photo = models.ImageField(upload_to='images/',blank=True)
    body = models.TextField()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post_detail',args=[str(self.id)])