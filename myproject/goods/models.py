from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='Url')

    class Meta:
        db_table: str = 'category'
        verbose_name: str = 'Категорию'
        verbose_name_plural: str = 'Категории'
