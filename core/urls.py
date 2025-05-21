from django.contrib import admin
from django.urls import path
from core.views.auth_views import CustomLoginView, CustomLogoutView
from core.views.dashboard import DashboardHomeView

from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

urlpatterns = [   
    path("admin/", admin.site.urls), 
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('', DashboardHomeView.as_view(), name='dashboard'),
]