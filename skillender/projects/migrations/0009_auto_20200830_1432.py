# Generated by Django 3.0.8 on 2020-08-30 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20200830_1352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='goal',
            new_name='goal_hours',
        ),
    ]