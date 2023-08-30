from django.db import models

class Alumno(models.Model):
    tutores = models.CharField(max_length=80)
    DNI_A = models.CharField(max_length=12)
    matricula = models.CharField(max_length=8)
    nombres_A = models.CharField(max_length=50)
    apellidos_A = models.CharField(max_length=40)
    tel_A = models.CharField(max_length=14)
    direccion_A = models.CharField(max_length=90)
    CUIL = models.CharField(max_length=14)
    copiaDNI_A = models.CharField(max_length=12,choices=[('entregado', 'Entregado'), ('no_entregado', 'No entregado')])
    fechanacimientoA = models.DateField()

    def __str__(self):
        return self.nombres_A + ' ' + self.apellidos_A
