from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Recipe(models.Model):
    recipe_name = models.CharField('Название', max_length=40)
    pub_date = models.DateTimeField('Дата публикации')
    description = models.TextField('Описание')
    mark = 0
    price = models.IntegerField('Примерная стоимость')

    def __str__(self):
        return self.recipe_name
    # не забыть добавить ценник для рецепта!


class FirstRecipe(Recipe):
    pass


class SecondRecipe(Recipe):
    pass


class EasyRecipe(Recipe):
    pass


class DesertRecipe(Recipe):
    pass
    

class SiteUser(User):
    photo = models.ImageField('Фото')


class Comment(models.Model):
    text = models.TextField('Текст комментария')
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)



