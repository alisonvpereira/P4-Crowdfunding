# Generated by Django 3.0.8 on 2020-09-27 08:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_customuserprofile_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuserprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]