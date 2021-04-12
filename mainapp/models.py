from django.db import models
from django.conf import settings
from django.core.cache import cache

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True, null=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_all(cls):
        if settings.LOW_CACHE:
            key = 'categories'
            categories = cache.get(key)
            if categories is None:
                categories = cls.objects.all()
                cache.set(key, categories)
            return categories
        else:
            return cls.objects.all()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()
        cache.delete('categories')


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя продукта', max_length=256)
    image = models.ImageField(upload_to='products_images', default='default.png')
    short_description = models.CharField(verbose_name='краткое описание продукта', max_length=128, blank=True)
    description = models.TextField(verbose_name='описание продукта', blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)

    def __str__(self):
        return f'{self.name} | {self.category.name}'
