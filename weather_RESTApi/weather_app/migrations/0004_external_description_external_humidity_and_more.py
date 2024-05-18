# Generated by Django 5.0.6 on 2024-05-18 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_app', '0003_external_weather_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='external',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='external',
            name='humidity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='external',
            name='temp_max',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='external',
            name='temp_min',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='external',
            name='temperature',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='external',
            name='wind_speed',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='external',
            name='city',
            field=models.CharField(max_length=100),
        ),
    ]
