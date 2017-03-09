from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=63)
    content = models.CharField(max_length=255)
    date_published = models.DateTimeField(blank=None, null=None)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title
