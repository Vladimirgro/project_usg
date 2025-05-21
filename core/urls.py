from django.contrib import admin
from django.urls import path
from core.views.auth_views import CustomLoginView, CustomLogoutView
from core.views.dashboard import DashboardHomeView

from core.views.user_views import (
    UserListView, UserCreateView, UserUpdateView, UserDeleteView
)

from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

urlpatterns = [       
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('', DashboardHomeView.as_view(), name='dashboard'),
]


urlpatterns += [
    path("usuarios/", UserListView.as_view(), name="user_list"),
    path("usuarios/nuevo/", UserCreateView.as_view(), name="user_create"),
    path("usuarios/<int:pk>/editar/", UserUpdateView.as_view(), name="user_update"),
    path("usuarios/<int:pk>/eliminar/", UserDeleteView.as_view(), name="user_delete"),
]