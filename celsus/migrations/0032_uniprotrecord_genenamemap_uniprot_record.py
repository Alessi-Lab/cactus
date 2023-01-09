# Generated by Django 4.1.1 on 2022-11-23 12:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('celsus', '0031_curtain_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniprotRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('gene_names', models.TextField()),
                ('record', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='genenamemap',
            name='uniprot_record',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='gene_map', to='celsus.uniprotrecord'),
        ),
    ]