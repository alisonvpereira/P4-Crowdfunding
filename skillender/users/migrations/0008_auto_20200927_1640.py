# Generated by Django 3.0.8 on 2020-09-27 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200927_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuserprofile',
            name='bio',
            field=models.TextField(blank='True', default=''),
        ),
        migrations.AddField(
            model_name='customuserprofile',
            name='image',
            field=models.URLField(blank=True),
        ),
    ]