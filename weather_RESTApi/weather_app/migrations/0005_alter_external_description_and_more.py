# Generated by Django 5.0.6 on 2024-05-18 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_app', '0004_external_description_external_humidity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='external',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='external',
            name='weather_url',
            field=models.URLField(null=True),
        ),
    ]