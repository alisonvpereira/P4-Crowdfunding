# Generated by Django 3.0.8 on 2020-08-30 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20200830_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(default='enter a description'),
            preserve_default=False,
        ),
    ]
