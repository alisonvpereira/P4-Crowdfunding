# Generated by Django 3.0.8 on 2020-09-29 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_auto_20200929_1509'),
        ('users', '0025_remove_profile_pledges'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='skills',
            field=models.ManyToManyField(blank=True, to='projects.Skill'),
        ),
    ]
