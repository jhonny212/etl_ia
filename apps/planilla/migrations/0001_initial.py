# Generated by Django 4.0.3 on 2022-04-04 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='REP_EMPRESA',
            fields=[
                ('id_empresa', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('nombre_empresa', models.CharField(max_length=50)),
                ('nit', models.PositiveIntegerField()),
                ('codigo', models.PositiveIntegerField()),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'REP_EMPRESA',
                'verbose_name_plural': 'REP_EMPRESAs',
            },
        ),
        migrations.CreateModel(
            name='REP_PERSONA',
            fields=[
                ('id_persona', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('dpi', models.PositiveIntegerField()),
                ('primer_nombre', models.CharField(max_length=300)),
                ('segundo_nombre', models.CharField(max_length=350)),
                ('primer_apellido', models.CharField(max_length=300)),
                ('segundo_apellido', models.CharField(max_length=300)),
                ('apellido_casada', models.CharField(max_length=300)),
                ('oden_cedula', models.PositiveIntegerField()),
                ('registro_cedula', models.PositiveIntegerField()),
                ('direccion_residencia', models.CharField(max_length=350)),
                ('nit', models.PositiveIntegerField()),
                ('genero', models.CharField(max_length=50)),
                ('telefono', models.PositiveIntegerField()),
                ('correo_electronico', models.CharField(max_length=250)),
                ('fecha_nacimiento', models.DateField()),
            ],
            options={
                'verbose_name': 'REP_PERSONA',
                'verbose_name_plural': 'REP_PERSONAs',
            },
        ),
        migrations.CreateModel(
            name='REP_TRABAJO',
            fields=[
                ('id_trabajo', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('fecha_inicial', models.DateField()),
                ('fecha_final', models.DateField()),
                ('nombre_puesto', models.CharField(max_length=350)),
                ('mes_planilla', models.CharField(max_length=350)),
                ('salario', models.PositiveIntegerField()),
                ('id_empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planilla.rep_empresa')),
                ('id_persona', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='planilla.rep_persona')),
            ],
            options={
                'verbose_name': 'REP_TRABAJO',
                'verbose_name_plural': 'REP_TRABAJOs',
            },
        ),
    ]
