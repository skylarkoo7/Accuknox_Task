from django.db import models

class Calculation(models.Model):
    operation = models.CharField(max_length=50)
    result = models.FloatField()

class Log(models.Model):
    message = models.CharField(max_length=255)
