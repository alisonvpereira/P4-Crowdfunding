from django.db import models
from django.contrib.auth import get_user_model
from users.models import CustomUser



class Skill(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a skill')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    description = models.TextField()

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a category')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    description = models.TextField()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal_hours = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )
    category = models.ManyToManyField(Category, help_text='Select a category for this project')
    

    def display_category(self):
        """Create a string for the Category. This is required to display category in Admin."""
        return ', '.join(category.name for category in self.category.all()[:3])
    
    display_category.short_description = 'Category'

class Pledge(models.Model):
    hours = models.IntegerField()
    skill = models.ManyToManyField(Skill, help_text='Select a skill for this project')
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='volunteer_pledges'
    )

    def display_skill(self):
        """Create a string for the Category. This is required to display category in Admin."""
        return ', '.join(skill.name for skill in self.skill.all()[:3])
    
    display_skill.short_description = 'Skill'



