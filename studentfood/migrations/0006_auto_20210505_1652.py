# Generated by Django 3.1.7 on 2021-05-05 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentfood', '0005_auto_20210504_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='price',
            field=models.IntegerField(null=True, verbose_name='Примерная стоимость'),
        ),
    ]
