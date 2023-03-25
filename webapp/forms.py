from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, BaseValidator



def max_len_validator(string):
    if len(string) > 20:
        raise ValidationError('Заголовок должен быть длиннее 2 символов')
    return string


class CustomLenValidator(BaseValidator):
    def __init__(self, limit_value=20):
        message = 'Максимальная длина заголовка %(limit_value)s. Вы ввели %(show_value)s символов'
        super().__init__(limit_value=limit_value, message=message)

    def compare(self, value, limit_value):
        print(value)
        print(limit_value)
        return value > limit_value

    def clean(self, value):
        return len(value)




class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False, label='Найти')
