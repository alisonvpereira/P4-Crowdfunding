# Generated by Django 3.0.8 on 2020-09-29 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_auto_20200926_1914'),
        ('users', '0022_profile_skill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='skill',
        ),
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=models.ManyToManyField(blank=True, to='projects.Skill'),
        ),
    ]
