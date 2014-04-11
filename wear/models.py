# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(u'Название', max_length=30)

    @models.permalink
    def get_absolute_url(self):
        return 'wear.views.wear_list_cat', [str(self.id)]

    class Meta():
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'

    def __unicode__(self):
        return u'%s' % (self.title, )


class Size(models.Model):
    title = models.CharField(u'Название', max_length=10)
    category = models.ForeignKey(Category)

    class Meta():
        verbose_name = u'Размер'
        verbose_name_plural = u'Размеры'
        ordering = ('title', )

    def __unicode__(self):
        return u'%s(%s)' % (self.title, self.category.title)


class Cloth(models.Model):
    title = models.CharField(u'Название', max_length=200)
    description = models.TextField(u'Описание', blank=True)
    price = models.IntegerField(u'Цена', )
    logo = models.ImageField(u'Основное изображение', upload_to="wear/galery/logos", blank=True)
    comment = models.TextField(u'Дополнительные комментарии', blank=True)
    category = models.ForeignKey(Category)
    rating_1 = models.IntegerField(u'Оценка 1', default=0)
    rating_2 = models.IntegerField(u'Оценка 2', default=0)
    rating_3 = models.IntegerField(u'Оценка 3', default=0)
    rating_4 = models.IntegerField(u'Оценка 4', default=0)
    rating_5 = models.IntegerField(u'Оценка 5', default=0)
    sizez = models.ManyToManyField(Size, through='SizeCount')

    @models.permalink
    def get_absolute_url(self):
        return 'wear.views.wear_detail', [str(self.id)]

    class Meta():
        verbose_name = u'Наименование'
        verbose_name_plural = u'Наименования'
        ordering = ('title', )

    def __unicode__(self):
        return u'%s' % self.title


class SizeCount(models.Model):
    size = models.ForeignKey(Size)
    item = models.ForeignKey(Cloth)
    count = models.IntegerField(u'Количество', default=0)

    class Meta():
        verbose_name = u'Размер'
        verbose_name_plural = u'Размеры'
        ordering = ('size', )

    def __unicode__(self):
        return u'%s' % self.size


class Gallery(models.Model):
    item = models.ForeignKey(Cloth)
    image = models.ImageField(u'Изображение', upload_to="wear/galery", blank=True)

    class Meta():
        verbose_name = u'Изображение'
        verbose_name_plural = u'Изображения'


class Comments(models.Model):
    item = models.ForeignKey(Cloth)
    text = models.TextField(u'Текст комментария', )

    class Meta():
        verbose_name = u'Комментарий'
        verbose_name_plural = u'Комментарии'

class Cart(models.Model):
    user = models.ForeignKey(User)
    items = models.ManyToManyField(Cloth, through='Proxy')
    first_name = models.CharField(u'Имя', max_length=30)
    last_name = models.CharField(u'Фамилия', max_length=30)
    addres = models.TextField(u'Адрес', )
    phone = models.CharField(u'Телефон', max_length=40)
    comments = models.TextField(u'Дополнительные комментарии', )
    total = models.IntegerField(u'Общая стоимость заказа', default=0)

    class Meta():
        verbose_name = u'Заказ'
        verbose_name_plural = u'Заказы'

class Contacts(models.Model):
    user = models.ForeignKey(User)
    addres = models.TextField(u'Адрес', )
    phone = models.CharField(u'Телефон', max_length=40)

    class Meta():
        verbose_name = u'Контактные данные'
        ordering = ('user', )


class Proxy(models.Model):
    item = models.ForeignKey(Cloth)
    cart = models.ForeignKey(Cart)
    count = models.IntegerField(u'Количество', )
    size = models.ForeignKey(Size)

    class Meta():
        verbose_name = u'Proxy'
        ordering = ('item', )