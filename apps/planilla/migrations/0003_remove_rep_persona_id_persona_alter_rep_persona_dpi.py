# Generated by Django 4.0.3 on 2022-04-05 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planilla', '0002_remove_rep_persona_apellido_casada_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rep_persona',
            name='id_persona',
        ),
        migrations.AlterField(
            model_name='rep_persona',
            name='dpi',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
