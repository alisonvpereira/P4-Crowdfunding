from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser , Profile
from projects.models import Project, Pledge




@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_joined', 'last_login')
    list_filter = ['is_superuser', 'is_staff']
    ordering = ['username']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display =['user', 'created_at', 'updated_at']
    list_filter = ['user__skills', 'user__is_staff', 'user__is_superuser']
