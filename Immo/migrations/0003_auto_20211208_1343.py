# Generated by Django 3.2.9 on 2021-12-08 12:43

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Immo', '0002_post_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='surface',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=9, validators=[django.core.validators.MinValueValidator(Decimal('1'))]),
        ),
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, validators=[django.core.validators.MinValueValidator(Decimal('1'))]),
        ),
    ]
