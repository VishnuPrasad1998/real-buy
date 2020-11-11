from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo_user = models.ImageField(upload_to='photos/user/propic', blank=False, default='photos/2020/10/30/avatar.jpeg')
    address = models.CharField(max_length=200, blank=False, default="sdsdsadsdasdasdasdsadasdsad")
    phone = models.CharField(max_length=200, blank=False, default="838848484")

    def __str__(self):
        return self.user.username