from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager): #Modelo personalizado para super usuario
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El email es obligatorio")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin): #Modelo personalizado de user para crear Tabla
    ROLES = [
                ('gerente', 'Gerente'),
                ('admin', 'Administrador'),
                ('medico', 'Médico'),
                ('asistente', 'Asistente'),
            ]

    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=50)
    apaterno = models.CharField(max_length=50)
    amaterno = models.CharField(max_length=50)
    rol = models.CharField(max_length=20, choices=ROLES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'rol']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
