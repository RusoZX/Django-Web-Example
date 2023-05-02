from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Notification(models.Model):
    MENSAJE = 'mensaje'
    LIKE = 'like'

    CHOICES = (
        (MENSAJE, 'Mensaje'),
        (LIKE, 'Like')
    )

    to_user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)

    notification_type  = models.CharField(max_length=20,choices=CHOICES)
    is_read = models.BooleanField(default=False)

    created_at= models.DateTimeField(auto_now_add=True)
    created_by= models.ForeignKey(User, related_name='creatednotifications', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']
