# Generated by Django 3.2.10 on 2022-01-27 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_catalogos', '0004_personas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dependencias',
            name='dependencia',
            field=models.CharField(max_length=50),
        ),
    ]