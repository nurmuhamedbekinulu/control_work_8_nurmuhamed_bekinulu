# Generated by Django 4.1.6 on 2023-03-25 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_product_remove_comment_article_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Удалено'),
        ),
    ]
