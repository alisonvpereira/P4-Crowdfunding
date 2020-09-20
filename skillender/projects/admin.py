from django.contrib import admin
from .models import Project, Pledge, Category, Skill


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['owner', 'title', 'display_category', 'is_open', 'date_created']
    list_filter = ("category","is_open")
    # search_fields = ['title', 'content']
    
@admin.register(Pledge)
class PledgeAdmin(admin.ModelAdmin):
    list_display = ['id', 'volunteer', 'anonymous', 'display_skill']
    list_filter = ("project__title", "skill", "anonymous")
    # search_fields = ['title', 'content']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description','updated_at']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'description','updated_at']