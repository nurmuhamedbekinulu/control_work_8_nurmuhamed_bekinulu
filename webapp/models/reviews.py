from django.db import models
from django.utils import timezone
from django.db.models import TextChoices
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User



class ReviewChoice(TextChoices):
    GREAT = 5
    FINE = 4
    SATISFACTORILY = 3
    BAD = 2
    TERRIBLE = 1
    NOT_RATED = 0


class Review(models.Model):
    author = models.ForeignKey(
        to=User,
        related_name='reviews',
        on_delete=models.CASCADE,
        verbose_name='Продукт'
    )
    product = models.ForeignKey(
        'webapp.Product',
        related_name='reviews',
        on_delete=models.CASCADE,
        verbose_name='Продукт'
    )
    review = models.TextField(
        max_length=3000,
        null=False,
        blank=False,
        verbose_name="Отзыв"
    )
    rating = models.CharField(
        verbose_name='Оценка',
        choices=ReviewChoice.choices,
        max_length=20,
        null=False,
        blank=False,
        default=ReviewChoice.NOT_RATED
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        null=False,
        default=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления"
    )
    deleted_at = models.DateTimeField(
        verbose_name='Дата и время удаления',
        null=True,
        default=None
    )

    def __str__(self):
        return f"{self.author} - {self.review}"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
