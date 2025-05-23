
# core/views/user_views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


from core.models.user import CustomUser
from core.forms.forms import (        # ajusta import si tus forms viven en otro módulo
    CustomUserCreationForm,
    CustomUserChangeForm,
)


@require_POST
def create_user_ajax(request):
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': True, 'message': 'Usuario creado exitosamente'})
    else:
        errors = form.errors.as_json()
        return JsonResponse({'success': False, 'errors': errors}, status=400)

# ---- LISTA ----
class UserListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model               = CustomUser
    template_name       = "users/user_list.html"
    context_object_name = "users"
    permission_required = "core.view_customuser"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CustomUserCreationForm()  # ← esto es clave para el modal
        return context

# ---- CREAR ----
class UserCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model         = CustomUser
    form_class    = CustomUserCreationForm
    template_name = "users/user_form.html"
    success_url   = reverse_lazy("user_list")
    permission_required = "core.add_customuser"

# ---- ACTUALIZAR ----
class UserUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model       = CustomUser
    form_class  = CustomUserChangeForm
    template_name = "users/user_form.html"
    success_url = reverse_lazy("user_list")
    permission_required = "core.change_customuser"

# ---- ELIMINAR ----
class UserDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model         = CustomUser
    template_name = "users/user_confirm_delete.html"
    success_url   = reverse_lazy("user_list")
    permission_required = "core.delete_customuser"
