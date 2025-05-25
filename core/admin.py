from django.contrib import admin
from .models.user import CustomUser

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core.forms.forms import CustomUserCreationForm, CustomUserChangeForm   # los creas en paso 4


@admin.register(CustomUser) #Registrar el modelo en el panel admin
class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form     = CustomUserChangeForm
    model    = CustomUser

    #Visualizacion en la lista de usuarios
    list_display  = ("email", "nombre", "apaterno", "amaterno", "rol", "is_active", "is_staff") #columnas en la tabla usuarios
    list_filter   = ("rol", "is_staff", "is_active") #filtros de lado derecho del admin
    search_fields = ("email", "nombre") #permite buscar por email o nombre
    ordering      = ("email",) #ordena por email

    #Campos que se muestran al editar un usuario
    fieldsets = (
        (None,               {"fields": ("email", "password")}),
        ("Información",      {"fields": ("nombre", "apaterno", "amaterno", "rol")}),
        ("Permisos",         {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Fechas importantes", {"fields": ("last_login",)}), #Fecha de ultimo inicio de sesion
    )

    #Campos que muestran al agregar un usuario
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "nombre", "apaterno", "amaterno", "rol", "password1", "password2", "is_active", "is_staff"),
        }),
    )

