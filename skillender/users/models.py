from django.contrib.auth.models import AbstractUser
from django.db import models
from projects.models import Skill



class CustomUser(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=80)
    website = models.URLField()
    image = models.URLField("Profile Picture", default='https://ringwooddental.com.au/wp-content/uploads/2018/05/profile-placeholder-f-e1526434202694.jpg', blank=True)
    bio = models.TextField(default='', blank=True)   
    phone = models.CharField(max_length=10, default='', blank='True')
    skill = models.ManyToManyField(Skill, default='', blank=True)


    
    def __str__(self):
        return self.username

    def display_skill(self):
        """Create a string for the Skill. This is required to display skill in Admin."""
        return ', '.join(skill.name for skill in self.skill.all()[:3])
    
    display_skill.short_description = 'Skill'

    

