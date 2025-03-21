from django.db import models

class Notas(models.Model):
    matematicas_o_historia = models.FloatField()
    lengua_y_litertura = models.FloatField()
    idioma = models.FloatField()
    prueba_especifica = models.FloatField()
    nota_media = models.FloatField()
    fecha = models.DateTimeField(auto_now_add=True)  # Asigna automáticamente la fecha y hora actuales al crear la instancia

    def __str__(self):
        return f"Notas - {self.nota_media}"
