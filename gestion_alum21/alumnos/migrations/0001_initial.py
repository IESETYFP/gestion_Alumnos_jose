# Generated by Django 4.2.4 on 2023-08-30 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutores', models.CharField(max_length=80)),
                ('DNI_A', models.CharField(max_length=12)),
                ('matricula', models.CharField(max_length=8)),
                ('nombres_A', models.CharField(max_length=50)),
                ('apellidos_A', models.CharField(max_length=40)),
                ('tel_A', models.CharField(max_length=14)),
                ('direccion_A', models.CharField(max_length=90)),
                ('CUIL', models.CharField(max_length=14)),
                ('copiaDNI_A', models.CharField(choices=[('entregado', 'Entregado'), ('no_entregado', 'No entregado')], max_length=12)),
                ('fechanacimientoA', models.DateField()),
            ],
        ),
    ]
