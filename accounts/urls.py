from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views_profile import edit_profile_view

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),
    path('edit-profile/', edit_profile_view, name='edit_profile'),
    path('', views.home_view, name='home'),
]
