from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, BaseValidator
from webapp.models import Product, Review



def max_len_validator(string):
    if len(string) > 20:
        raise ValidationError('Заголовок должен быть длиннее 2 символов')
    return string


class CustomLenValidator(BaseValidator):
    def __init__(self, limit_value=200):
        message = 'Максимальная длина заголовка %(limit_value)s. Вы ввели %(show_value)s символов'
        super().__init__(limit_value=limit_value, message=message)

    def compare(self, value, limit_value):
        print(value)
        print(limit_value)
        return value > limit_value

    def clean(self, value):
        return len(value)

class ProductForm(forms.ModelForm):
    name = forms.CharField(
        validators=(MinLengthValidator(limit_value=2, message='Нужно ввести как  минимум 2 символа'), CustomLenValidator()))

    class Meta:
        model = Product
        fields = ('name', 'category', 'description', 'pic')
        labels = {
            'name': 'Название продукта',
            'category': 'Категория',
            'description': 'Описание',
            'pic': 'Картинка'
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise ValidationError('Название должено быть длиннее 2 символов')
        if Product.objects.filter(name=name).exists():
            raise ValidationError('Продукт с таким название уже есть')
        return name


class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False, label='Найти')


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('author', 'review', 'rating')
        labels = {
            'author': 'Автор',
            'review': 'Отзыв',
            'rating': 'Оценка'
        }
