# Generated by Django 3.0.8 on 2020-09-28 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20200928_1059'),
    ]

    operations = [

        migrations.AddField(
            model_name='customuser',
            name='skill',
            field=models.CharField(default='Add', max_length=80),
            preserve_default=False,
        ),
    ]
