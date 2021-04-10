from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length = 255, verbose_name = 'Category Name')
    slug = models.SlugField(unique = True)

    def __str__(self):
        return self.name


class Product(models.Model):
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
