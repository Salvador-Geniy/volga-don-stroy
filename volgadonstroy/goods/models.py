from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Good(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True,
                                 on_delete=models.SET_NULL, related_name='products')
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    in_stock = models.BooleanField(default=False)
    published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'


class Images(models.Model):
    good = models.OneToOneField(Good, on_delete=models.CASCADE)
    img1 = models.ImageField(upload_to='products/', null=True, blank=True)
    img2 = models.ImageField(upload_to='products/', null=True, blank=True)
    img3 = models.ImageField(upload_to='products/', null=True, blank=True)
    img4 = models.ImageField(upload_to='products/', null=True, blank=True)
    img5 = models.ImageField(upload_to='products/', null=True, blank=True)
