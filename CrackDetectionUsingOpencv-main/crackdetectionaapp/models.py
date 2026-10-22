from django.db import models

# Create your models here.

class crackdetect(models.Model):
    img = models.ImageField(upload_to='images/')
    




