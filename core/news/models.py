from django.db import models
from django.urls import reverse


class Post(models.Model):
   
    title = models.CharField(max_length=250, unique=True)
    image = models.CharField(max_length=250, null=True)
    content = models.TextField(null=True)
    date = models.DateTimeField(null=True)
    url = models.CharField(max_length=250, null=True)
    
    def __str__(self):
        return self.title

    objects = models.Manager() # The default manager.