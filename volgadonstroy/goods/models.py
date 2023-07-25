from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Good(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='goods/%Y/%m/%d', default='goods/2023/07/25/no-image-icon-23485.png')

    def __str__(self):
        return self.name
