# Generated by Django 3.0.8 on 2020-09-20 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_auto_20200920_1447'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pledge',
            options={'ordering': ['owner__username']},
        ),
    ]