# Generated by Django 3.1.7 on 2021-05-22 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentfood', '0007_auto_20210511_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото рецепта'),
        ),
    ]