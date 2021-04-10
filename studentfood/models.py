from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

global_category = [
    'Первые блюда',
    'Вторые блюда',
    'Закуски/Салаты',
    'Сладкое/Десерты'
]


class Recipe(models.Model):
    recipe_name = models.CharField('Название', max_length=40)
    pub_date = models.DateTimeField('Дата публикации')
    description = models.TextField('Описание')
    mark = 0
    price = models.IntegerField('Примерная стоимость')
    category = models.CharField('Категория', max_length=30)

    def __str__(self):
        return self.recipe_name
    # не забыть добавить ценник для рецепта!


class User(AbstractUser):
    photo = models.ImageField('Фото')


class Comment(models.Model):
    text = models.TextField('Текст комментария')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)



