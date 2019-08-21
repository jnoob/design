from django.db import models

# Create your models here.
class PasteContent(models.Model):

    content = models.CharField(max_length=3000)
    expire_at = models.DateTimeField()
    link = models.CharField(max_length=200)
