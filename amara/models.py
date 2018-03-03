from django.db import models


# Create your models here.

class Collection(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    protocol = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    platform = models.CharField(max_length=100)
    keeper = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
