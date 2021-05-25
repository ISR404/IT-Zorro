# Generated by Django 3.1.7 on 2021-05-25 10:16

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentfood', '0012_merge_20210525_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(blank=True, default='recipe_img/no_photo.jpg', null=True, upload_to='recipe_img', verbose_name='Фото рецепта'),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(default='user_img/no_photo.jpg', upload_to='user_img', verbose_name='Фото'),
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark_value', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentfood.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
