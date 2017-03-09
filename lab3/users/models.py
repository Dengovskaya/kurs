from django.conf import settings
from django.db import models
from .storage import OverwriteStorage



def profile_pic_path(instance, filename):
    return '/'.join(['content', 'user_' + str(instance.id), 'profile_pic.jpg'])

class UserInfo(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=30, default='first name')
    surname = models.CharField(max_length=30, default='second name')
    phone = models.CharField(max_length=20, blank=True)
    about = models.CharField(max_length=255, blank=True)
    profile_image = models.ImageField(blank=True,  storage=OverwriteStorage(), upload_to=profile_pic_path)

    def __str__(self):
        return self.name + ' ' + self.user.email
