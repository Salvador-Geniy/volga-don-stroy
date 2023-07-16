from django.db import models


class Good(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='goods/%Y/%m/%d')

    def __str__(self):
        return self.name
