# Generated by Django 3.1.7 on 2021-04-28 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentfood', '0002_auto_20210423_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(null=True, upload_to='', verbose_name='Фото рецепта'),
        ),
    ]