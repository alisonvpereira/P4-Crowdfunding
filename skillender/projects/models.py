from django.db import models
from django.contrib.auth import get_user_model




class Skill(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a skill')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    description = models.TextField()
    image = models.URLField()

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"        
        ordering = ['name']
        
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a category')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    description = models.TextField()
    image = models.URLField()

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
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now =True)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )
    category = models.ManyToManyField(Category, help_text='Select a category for this project', related_name='projects')
    

    def display_category(self):
        """Create a string for the Category. This is required to display category in Admin."""
        return ', '.join(category.name for category in self.category.all()[:3])
    
    display_category.short_description = 'Category'

    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return self.title

class Pledge(models.Model):
    hours = models.IntegerField()
    skill = models.ManyToManyField(Skill, help_text='Select a skill for this project', related_name='pledges')
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now =True)
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='pledges'
    )


    def volunteer(self):
        return self.owner.username

    def username(self):
        return self.owner.username

    def project_title(self):
        return self.project.title

    def display_skill(self):
        """Create a string for the Skill. This is required to display skill in Admin."""
        return ', '.join(skill.name for skill in self.skill.all()[:3])
    
    display_skill.short_description = 'Skill'

    class Meta:
        ordering = ['id']



