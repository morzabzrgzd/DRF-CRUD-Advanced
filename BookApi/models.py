from django.db import models
from datetime import datetime

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=150)
    store_name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(default='', upload_to='store_image/', null=True)
    fav = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
