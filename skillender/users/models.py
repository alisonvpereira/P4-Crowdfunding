from django.contrib.auth.models import AbstractUser
from django.db import models
from projects.models import Skill
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class CustomUser(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=80)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        blank=True,
        on_delete=models.CASCADE,
    )
    fullname = models.CharField('Full Name',
                                max_length=50,
                                blank=True,
                                null=True)
    bio = models.TextField('Biography',
                           default='Tell us about yourself...',
                           blank=True)
    website = models.URLField(
        'Website',
        default=
        'https://via.placeholder.com/728x90.png?text=Website+coming+soon',
        blank=True)
    image = models.URLField(
        'Profile Picture',
        default='https://static.productionready.io/images/smiley-cyrus.jpg',
        blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    skills = models.ManyToManyField(Skill, blank=True)

    def display_skill(self):
        """Create a string for the Skill. This is required to display category in Admin."""
        return ', '.join(skills.name for skills in self.skills.all()[:3])

    display_skill.short_description = 'Skills'

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=CustomUser)
def create_related_profile(sender, instance, created, *args, **kwargs):
    if instance and created:
        instance.profile = Profile.objects.create(user=instance)


def delete_user(sender, instance=None, **kwargs):
    try:
        instance.user
    except User.DoesNotExist:
        pass
    else:
        instance.user.delete()
post_delete.connect(delete_user, sender=Profile)
