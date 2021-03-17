# Generated by Django 3.1.7 on 2021-03-17 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=40, verbose_name='Название')),
                ('pub_date', models.DateTimeField(verbose_name='Дата публикации')),
                ('description', models.TextField(verbose_name='Описание')),
                ('mark', models.FloatField(verbose_name='Оценка')),
                ('on_favorite', models.BooleanField(verbose_name='В избранном')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Никнейм')),
                ('photo', models.ImageField(upload_to='', verbose_name='Фото')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentfood.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentfood.user')),
            ],
        ),
    ]
