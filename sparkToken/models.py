from django.db import models

# Create your models here.
class sparkToken(models.Model):
    token = models.CharField(max_length=200)
    valid_till = models.DateTimeField()
    locked = models.BooleanField(default=False)
