# Generated by Django 4.1.1 on 2022-12-05 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celsus', '0038_project_default_settings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectsettings',
            name='data',
            field=models.TextField(default='{}'),
        ),
    ]
