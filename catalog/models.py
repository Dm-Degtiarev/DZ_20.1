from django.db import models


NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    product_name = models.CharField(max_length=200, verbose_name='Наименование')
    product_info = models.CharField(max_length=300, verbose_name='Описание')
    product_image = models.ImageField(upload_to='products/', verbose_name='Изображение', **NULLABLE)
    product_category = models.CharField(max_length=200, verbose_name='Категория')
    product_price = models.FloatField(max_length=20, verbose_name='Цена')
    product_create_date = models.DateField(verbose_name='Дата создания')
    product_last_upd_dt = models.DateField(verbose_name='Дата последнего изменения')

    def __str__(self):
        return f"{self.pk} - {self.product_name}"

    class Meta:

        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Наименование')
    category_info = models.CharField(max_length=300, verbose_name='Описание категории')
    # created_dt = models.DateField(verbose_name='Дата создания', **NULLABLE)

    def __str__(self):
        return f"{self.pk} - {self.category_name}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Contacts(models.Model):
    contact_name = models.CharField(max_length=100, verbose_name='Наименование')
    contact_number = models.CharField(max_length=17, verbose_name='Телефонный номер')

    def __str__(self):
        return f"{self.pk} - {self.contact_name}"

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
