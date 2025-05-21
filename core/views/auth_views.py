from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from core.forms.auth_forms import CustomAuthForm
from django.contrib import messages




class CustomLoginView(LoginView):
    template_name = 'auth/login.html'
    authentication_form = CustomAuthForm
    #redirect_authenticated_user = True
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar Sesión'
        return context
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        # Agregar mensaje de error personalizado
        messages.error(self.request, 'Credenciales incorrectas. Por favor intenta nuevamente.')
        return response

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
