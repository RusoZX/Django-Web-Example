from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Conversacion(models.Model):
    users = models.ManyToManyField(User, related_name='conversacion')
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-modified_at']

class Mensaje(models.Model):
    conversacion = models.ForeignKey(Conversacion, related_name='mensajes', on_delete=models.CASCADE)
    contenido = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='mensajes', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        self.conversacion.save()

        super(Mensaje, self).save(*args, **kwargs)