# Generated by Django 3.1.7 on 2021-04-21 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentfood', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
