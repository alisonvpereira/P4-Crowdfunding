# Generated by Django 3.0.8 on 2020-09-28 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20200928_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='skill',
        ),
    ]
