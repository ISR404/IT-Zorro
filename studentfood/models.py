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

# подписать поля


class Recipe(models.Model):  # рецепт
    recipe_name = models.CharField('Название', max_length=40)  # название рецепта
    pub_date = models.DateTimeField('Дата публикации')  # дата публикация
    description = models.TextField('Описание')  # описание рецепта
    mark = 0  # оценка рецепта
    price = models.IntegerField('Примерная стоимость')
    category = models.CharField('Категория', max_length=30)

    def __str__(self):  # при запросе класса выводит название рецепта
        return self.recipe_name

    def calculate_mark(self):  # реализовать оценку
        pass


class User(AbstractUser):
    photo = models.ImageField('Фото')  # список всех полей есть в файле миграции.

    def create_recipe(self, recipe_name, description, price, category):  # по идее параметры для функции должны браться
        #  из полей фронта, а потом на их основе выполняется функция создания и привязки рецепта к юзеру
        self.recipe_set.create(recipe_name=recipe_name, description=description, price=price, category=category)


class Comment(models.Model):
    text = models.TextField('Текст комментария')
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # связь комментария с пользователем
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)  # связь комментария с рецептом



