from django.db import models

# Create your models here.
class Tutorial(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank= False, default='')
    published = models.BooleanField(default=True)
