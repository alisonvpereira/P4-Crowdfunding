# Generated by Django 3.0.8 on 2020-09-29 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_customuser_skills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='skills',
        ),
    ]