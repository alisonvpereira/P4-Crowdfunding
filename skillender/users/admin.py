from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser 
from projects.models import Project, Pledge

class CustomUserInstanceInline(admin.TabularInline):
    model = Project

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ('username', 'last_name', 'first_name', 'date_of_birth')
#     # fields = ('first_name', 'last_name', 'date_of_birth')
#     inlines = [CustomUserInstanceInline]


admin.site.register(CustomUser)
