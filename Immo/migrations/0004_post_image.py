# Generated by Django 3.2.9 on 2021-12-10 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Immo', '0003_auto_20211208_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
