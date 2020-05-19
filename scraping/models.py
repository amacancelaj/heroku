from django.db import models
from django.utils import timezone

# Create your models here.

class PortalWebScrappingEmpleo(models.Model):
    url = models.CharField(max_length=250, unique=True)
    title = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['title']
    class Admin:
        pass