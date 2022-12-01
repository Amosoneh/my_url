from django.db import models


# Create your models here.

class UrlShortener(models.Model):
    longurl = models.URLField(max_length=225)
    shorturl = models.CharField(max_length=30)

    def __str__(self):
        return self.shorturl
