# Generated by Django 3.0.8 on 2020-09-27 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200927_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuserprofile',
            name='image',
            field=models.URLField(blank=True, default='https://ringwooddental.com.au/wp-content/uploads/2018/05/profile-placeholder-f-e1526434202694.jpg', verbose_name='Profile Picture'),
        ),
    ]
