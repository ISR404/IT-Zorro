from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

# подписать поля


class User(AbstractUser):
    photo = models.ImageField('Фото', null=True)  # список всех полей есть в файле миграции.

    def create_recipe(self, recipe_name, description, price, category):  # по идее параметры для функции должны браться
        #  из полей фронта, а потом на их основе выполняется функция создания и привязки рецепта к юзеру
        self.recipe_set.create(recipe_name=recipe_name, description=description, price=price, category=category, pub_date=timezone.now())


class Recipe(models.Model):  # рецепт
    recipe_name = models.CharField('Название', max_length=40)  # название рецепта
    pub_date = models.DateTimeField('Дата публикации')  # дата публикация
    description = models.TextField('Описание')  # описание рецепта
    avg_mark = 0  # оценка рецепта
    count_of_submits = 0  # количество людей, поставивших оценку
    price = models.IntegerField('Примерная стоимость')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    GLOBAL_CATEGORY = [
        ('first', 'Первые блюда'),
        ('second', 'Вторые блюда'),
        ('snack', 'Закуски/Салаты'),
        ('sweet', 'Сладкое/Десерты'),
    ]
    category = models.CharField('Категория', choices=GLOBAL_CATEGORY, max_length=16, blank=True)
    photo = models.ImageField('Фото рецепта', null=True)  # доделать в плане обязательности

    def __str__(self):  # при запросе класса выводит название рецепта
        return self.recipe_name

    def calculate_mark(self):  # реализовать оценку
        pass

    def set_mark(self):  # проверить авторизацию пользователя

        pass
    # def leave_comment(self, text):
        # user = User.objects.get()
        # self.comment_set.create(text=text)


class Comment(models.Model):
    text = models.CharField('Текст комментария', max_length=1500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # связь комментария с пользователем
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)  # связь комментария с рецептом
    pub_date = models.DateTimeField('Опубликовано', default=timezone.now)

    """
    def leave_comment(self):
        com = Comment()
        recipe = Recipe.objects.get(pk=...)
        user = User.objects.get(...)  # request во view
        text = 'some text'
        com.recipe = recipe
        com.user = user
        com.text = text  # на будущее
        com.save()
    """


