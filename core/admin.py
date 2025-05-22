from django.contrib import admin
from .models.user import CustomUser

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core.forms.forms import CustomUserCreationForm, CustomUserChangeForm   # los creas en paso 4


@admin.register(CustomUser)
class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form     = CustomUserChangeForm
    model    = CustomUser

    list_display  = ("email", "nombre", "apaterno", "amaterno", "rol", "is_active", "is_staff")
    list_filter   = ("rol", "is_staff", "is_active")
    search_fields = ("email", "nombre")
    ordering      = ("email",)

    fieldsets = (
        (None,               {"fields": ("email", "password")}),
        ("Información",      {"fields": ("nombre", "apaterno", "amaterno", "rol")}),
        ("Permisos",         {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Fechas importantes", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "nombre", "apaterno", "amaterno" "rol", "password1", "password2", "is_active", "is_staff"),
        }),
    )

