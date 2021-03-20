from django.db import models
from django.utils import timezone

# Create your models here.


class Recipe(models.Model):
    recipe_name = models.CharField('Название', max_length=40)
    pub_date = models.DateTimeField('Дата публикации')
    description = models.TextField('Описание')
    mark = 0

    def __str__(self):
        return self.recipe_name
    # не забыть добавить ценник для рецепта!
    

class User(models.Model):
    name = models.CharField('Никнейм', max_length=10)
    photo = models.ImageField('Фото')
    email = models.EmailField('Почта')
    # password = models.PasswordField


class Comment(models.Model):
    text = models.TextField('Текст комментария')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)



