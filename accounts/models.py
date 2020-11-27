from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo_user = ResizedImageField(size=[600, 600], upload_to='photos/user/propic', blank=False, default='photos/2020/10/30/avatar.jpeg')
    address = models.CharField(max_length=200, blank=False, default="Palarivattam, Cochin")
    phone = models.CharField(max_length=200, blank=False, default="7839939939")

    def __str__(self):
        return self.user.username