from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


User = get_user_model()


class Comic(models.Model):
    '''Модель для комиксов.'''
    title = models.CharField('Название комикса', max_length=200)
    author = models.CharField('Автор комикса', max_length=200)

    @property
    def rating(self):
        return self.ratings.all().aggregate(models.Avg('VALUE'))['VALUE__avg']

    class Meta:
        verbose_name = "Комикс"
        verbose_name_plural = "Комиксы"
        constraints = (models.UniqueConstraint(
            fields=("title", "author"),
            name="unique_comic"
        ),)

    def __str__(self):
        return self.title


class Rating(models.Model):
    '''Модель для рейтингов.'''
    comic_id = models.ForeignKey(
        Comic,
        on_delete=models.CASCADE,
        related_name='ratings',
        verbose_name='Комикс'
    )
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='ratings',
        verbose_name='Пользователь'
    )
    VALUE = models.PositiveSmallIntegerField(
        'Рейтинг',
        validators=(MinValueValidator(1), MaxValueValidator(5))
    )

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"
        constraints = (models.UniqueConstraint(
            fields=("comic_id", "user_id"),
            name="unique_rating"
        ),)

    def __str__(self):
        return f'{self.comic_id.title} — {self.user_id}'
