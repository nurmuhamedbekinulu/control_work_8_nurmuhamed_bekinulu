from django.db import models
from django.utils import timezone
from django.db.models import TextChoices



class CategoryChoice(TextChoices):
    GROCERY = 'Grocery', 'Бакалея'
    BEVERAGES = 'Beverages', 'Напитки'
    HOUSEHOLD_CHEMICALS = 'Household chemicals', 'Бытовая химия'
    OTHERS = 'Others', 'Разное'


class Product(models.Model):
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Название"
    )
    category = models.CharField(
        verbose_name='Категория',
        choices=CategoryChoice.choices,
        max_length=20,
        default=CategoryChoice.OTHERS)
    description = models.TextField(
        max_length=3000,
        null=False,
        blank=False,
        verbose_name="Текст"
    )
    pic = models.ImageField(
        null=True,
        blank=True,
        upload_to='product_pic',
        default='/product_pic/unregistered_user_ava.png',
        verbose_name='Картинка'
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
        return f"{self.name} - {self.description}"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
