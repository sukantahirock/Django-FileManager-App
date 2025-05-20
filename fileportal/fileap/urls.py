# fileapp/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='fileap/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('upload/', views.upload_file, name='file-upload'),
    path('files/', views.file_list, name='file-list'),
    path('download/<int:file_id>/', views.download_file, name='file-download'),
    path('delete/<int:file_id>/', views.delete_file, name='file-delete'),
    path('admin-panel/', views.admin_panel, name='admin-panel'),
]
