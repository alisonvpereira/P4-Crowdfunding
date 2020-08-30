# Generated by Django 3.0.8 on 2020-08-30 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20200824_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a category', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.ManyToManyField(help_text='Select a category for this project', to='projects.Category'),
        ),
    ]
