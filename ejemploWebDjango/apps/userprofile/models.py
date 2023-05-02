from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField('self', related_name='liked_by', symmetrical=False)
    avatar = models.ImageField(upload_to='uploads/', blank=True, null=True)
    
User.userprofile = property(lambda u:UserProfile.objects.get_or_create(user=u)[0])