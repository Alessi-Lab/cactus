# Generated by Django 4.1.1 on 2022-10-21 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('celsus', '0014_remove_comparison_file_file_comparison'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='comparison',
        ),
        migrations.AddField(
            model_name='comparison',
            name='file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comparisons', to='celsus.file'),
        ),
    ]
