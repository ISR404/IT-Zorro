# Generated by Django 3.1.7 on 2021-05-04 15:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('studentfood', '0004_auto_20210504_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Опубликовано'),
        ),
    ]
