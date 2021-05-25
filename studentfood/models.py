from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

# подписать поля


class User(AbstractUser):
    photo = models.ImageField('Фото', default='user_img/no_photo.jpg', upload_to='user_img')  # установлена стандартная фотография. пользовательские фото будут загружены в media/user_img

    def create_recipe(self, recipe_name, description, price, category):  # по идее параметры для функции должны браться
        #  из полей фронта, а потом на их основе выполняется функция создания и привязки рецепта к юзеру
        self.recipe_set.create(recipe_name=recipe_name, description=description, price=price, category=category, pub_date=timezone.now())

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url


class Recipe(models.Model):  # рецепт
    recipe_name = models.CharField('Название', max_length=40)  # название рецепта
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)  # дата публикация
    description = models.TextField('Описание')  # описание рецепта
    price = models.IntegerField('Примерная стоимость', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    GLOBAL_CATEGORY = [
        ('first', 'Первые блюда'),
        ('second', 'Вторые блюда'),
        ('snack', 'Закуски/Салаты'),
        ('sweet', 'Сладкое/Десерты'),
    ]
    category = models.CharField('Категория', choices=GLOBAL_CATEGORY, max_length=16, blank=True)
    photo = models.ImageField('Фото рецепта', default='recipe_img/no_photo.jpg', null=True, blank=True, upload_to='recipe_img')  # фото будут храниться по пути /media/recipe_img (не забудь создать эти папки перед тестом)

    def __str__(self):  # при запросе класса выводит название рецепта
        return self.recipe_name

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def calculate_mark(self):  # реализовать оценку
        max_marks = self.mark_set.all()
        sum_marks = 0
        for get_mark in max_marks:
            sum_marks += get_mark.mark_value
        avg_mark = sum_marks/len(max_marks)
        return avg_mark


    # def set_mark(self):  # проверить авторизацию пользователя
    #
    #     pass


class Comment(models.Model):
    text = models.CharField('Текст комментария', max_length=1500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # связь комментария с пользователем
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)  # связь комментария с рецептом
    pub_date = models.DateTimeField('Опубликовано', default=timezone.now)


class Mark(models.Model):
    USER_MARK_SET = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]
    mark_value = models.FloatField(choices=USER_MARK_SET, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('recipe', 'user')

    # def __str__(self):
    #     return str('Оценка к рецепту ' + self.recipe + ' пользоветелем ' + self.user)
