# Generated by Django 4.1.1 on 2022-11-05 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celsus', '0021_alter_differentialanalysisdata_gene_names_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='differentialanalysisdata',
            name='peptide_sequence',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='differentialanalysisdata',
            name='probability_score',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='differentialanalysisdata',
            name='ptm_data',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='differentialanalysisdata',
            name='ptm_position',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='differentialanalysisdata',
            name='ptm_position_in_peptide',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='differentialanalysisdata',
            name='sequence_window',
            field=models.TextField(null=True),
        ),
    ]
