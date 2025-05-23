from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from core.models.user import CustomUser
 
class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}))
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}))

    class Meta:
        model  = CustomUser
        fields = ["email", "nombre", "apaterno", "amaterno", "rol"]
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': True, 'autocomplete': 'off'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'apaterno': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'amaterno': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'rol': forms.Select(attrs={'class': 'form-control', 'required': True}),            
        }
        

    def clean_password2(self):
        p1 = self.cleaned_data.get("password1")
        p2 = self.cleaned_data.get("password2")
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return p2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class CustomUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model  = CustomUser
        fields = ("email", "nombre", "apaterno", "amaterno", "rol", "is_active", "is_staff")
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apaterno': forms.TextInput(attrs={'class': 'form-control'}),
            'amaterno': forms.TextInput(attrs={'class': 'form-control'}),
            'rol': forms.Select(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
        
    