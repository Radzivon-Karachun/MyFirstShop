from django.db import models
from PIL import Image


class MinResolutionErrorException(Exception):
    pass


class MaxResolutionErrorException(Exception):
    pass


class MaxSizeErrorException(Exception):
    pass


class Categories(models.Model):
    name = models.CharField(max_length = 255, verbose_name = 'Category Name')
    slug = models.SlugField(unique = True)

    def __str__(self):
        return self.name


class Product(models.Model):

    MIN_RESOLUTION = (400, 400)
    MAX_RESOLUTION = (1000, 1000)
    MAX_IMAGE_SIZE = 3145728

    class Meta:
        abstract = True

    category = models.ForeignKey(Categories, verbose_name = 'Category', on_delete = models.CASCADE)
    title = models.CharField(max_length = 255, verbose_name = 'Model')
    slug = models.SlugField(unique = True)
    image = models.ImageField(verbose_name = 'Pictures')
    description = models.TextField(verbose_name = 'Description', null = True)
    price = models.DecimalField(max_digits = 9, decimal_places = 2, verbose_name = 'Price')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        image = self.image
        img = Image.open(image)
        min_height, min_width = self.MIN_RESOLUTION
        max_height, max_width = self.MAX_RESOLUTION
        if image.size > Product.MAX_IMAGE_SIZE:
            raise MaxSizeErrorException('Image size should not exceed 3MB!')
        if img.height < min_height or img.width < min_width:
            raise MinResolutionErrorException('Image resolution less than the minimum!')
        elif img.height > max_height or img.width > max_width:
            raise MaxResolutionErrorException('Image resolution is greater than maximum!')
        super().save(*args, **kwargs)
