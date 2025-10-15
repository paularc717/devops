from django.db import models
 
class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
 
    def as_dict(self):
        return {"codigo": self.id, "nombre": self.nombre}
 
    def __str__(self):
        return f"{self.id} - {self.nombre}"
