# Generated by Django 3.1.1 on 2021-04-09 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Pictures')),
                ('description', models.TextField(null=True, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Price')),
                ('display_diagonal', models.CharField(max_length=255, verbose_name='Diagonal display')),
                ('display_type', models.CharField(max_length=255, verbose_name='Display type')),
                ('display_resolution', models.CharField(max_length=255, verbose_name='Display resolution')),
                ('battery_volume', models.CharField(max_length=255, verbose_name='Battery volume')),
                ('processor_freq', models.CharField(max_length=255, verbose_name='Frequency processor')),
                ('ram', models.CharField(max_length=255, verbose_name='RAM')),
                ('sd_card', models.BooleanField(default=True)),
                ('sd_card_volume_max', models.CharField(max_length=255, verbose_name='Max volume SD-Card')),
                ('qty_sim', models.DecimalField(decimal_places=0, max_digits=1, verbose_name='SIM Quantity')),
                ('rear_cam_mp', models.CharField(max_length=255, verbose_name='Rear camera resolution')),
                ('front_cam_mp', models.CharField(max_length=255, verbose_name='Front camera resolution')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Pictures')),
                ('description', models.TextField(null=True, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Price')),
                ('diagonal', models.CharField(max_length=255, verbose_name='Diagonal')),
                ('display_type', models.CharField(max_length=255, verbose_name='Display type')),
                ('processor_freq', models.CharField(max_length=255, verbose_name='Frequency processor')),
                ('ram', models.CharField(max_length=255, verbose_name='RAM')),
                ('video', models.CharField(max_length=255, verbose_name='Video card')),
                ('time_without_charge', models.CharField(max_length=255, verbose_name='Battery operating time')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
