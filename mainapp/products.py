from django.db import models
from .abstracts import Product


class Notebook(Product):
    diagonal = models.CharField(max_length = 255, verbose_name = 'Diagonal')
    display_type = models.CharField(max_length = 255, verbose_name = 'Display type')
    processor_freq = models.CharField(max_length = 255, verbose_name = 'Frequency processor')
    ram = models.CharField(max_length = 255, verbose_name = 'RAM')
    video = models.CharField(max_length = 255, verbose_name = 'Video card')
    time_without_charge = models.CharField(max_length = 255, verbose_name = 'Battery operating time')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)


class Smartphone(Product):
    display_diagonal = models.CharField(max_length = 255, verbose_name = 'Diagonal display')
    display_type = models.CharField(max_length = 255, verbose_name = 'Display type')
    display_resolution = models.CharField(max_length = 255, verbose_name = 'Display resolution')
    screen_refresh_rate = models.CharField(max_length = 255, verbose_name = 'Screen refresh rate')
    operating_system = models.CharField(max_length = 255, verbose_name = 'Operating system')
    processor = models.CharField(max_length = 255, verbose_name = 'Processor')
    ram = models.CharField(max_length = 255, verbose_name = 'Memory RAM')
    rom = models.CharField(max_length = 255, verbose_name = 'Built-in memory')
    sd_card = models.BooleanField(default = True)
    rear_cam_mp = models.CharField(max_length = 255, verbose_name = 'Rear camera resolution')
    front_cam_mp = models.CharField(max_length = 255, verbose_name = 'Front camera resolution')
    battery_capacity = models.CharField(max_length = 255, verbose_name = 'Battery capacity')
    dual_sim = models.BooleanField(default = True)

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)
