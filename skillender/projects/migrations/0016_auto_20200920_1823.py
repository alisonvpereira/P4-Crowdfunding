# Generated by Django 3.0.8 on 2020-09-20 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_auto_20200920_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='pledge',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
