from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','email','age','matricula','carrera','semestre','nombre','apellido')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username','email','age','matricula','carrera','semestre','nombre','apellido')
 

#Meta class to override the default fields by setting the model to out CustumUser
