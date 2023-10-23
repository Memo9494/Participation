from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email','username','age','is_staff','matricula','carrera','semestre','nombre','apellido',]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields':('age','matricula','carrera','semestre','nombre','apellido')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields':('age','matricula','carrera','semestre','nombre','apellido')}),
    )
admin.site.register(CustomUser, CustomUserAdmin)
