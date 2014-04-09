# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=30)

    class Meta():
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'

    def __unicode__(self):
        return u'%s' % (self.title, )


class Size(models.Model):
    title = models.CharField(max_length=10)
    category = models.ForeignKey(Category)

    class Meta():
        verbose_name = u'Размер'
        verbose_name_plural = u'Размеры'
        ordering = ('title', )

    def __unicode__(self):
        return u'%s(%s)' % (self.title, self.category.title)


class Cloth(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    logo = models.ImageField(upload_to="wear/galery/logos", blank=True)
    comment = models.TextField(blank=True)
    category = models.ForeignKey(Category)
    rating_1 = models.IntegerField(default=0)
    rating_2 = models.IntegerField(default=0)
    rating_3 = models.IntegerField(default=0)
    rating_4 = models.IntegerField(default=0)
    rating_5 = models.IntegerField(default=0)
    sizez = models.ManyToManyField(Size, through='SizeCount')

    class Meta():
        verbose_name = u'Наименование'
        verbose_name_plural = u'Наименования'
        ordering = ('title', )

    def __unicode__(self):
        return u'%s' % (self.title)


class SizeCount(models.Model):
    size = models.ForeignKey(Size)
    item = models.ForeignKey(Cloth)
    count = models.IntegerField(default=0)

    class Meta():
        verbose_name = u'Количество размеров'
        ordering = ('title', )


class Gallery(models.Model):
    item = models.ForeignKey(Cloth)
    image = models.ImageField(upload_to="wear/galery", blank=True)

    class Meta():
        verbose_name = u'Изображение'
        verbose_name_plural = u'Изображения'


class Comments(models.Model):
    item = models.ForeignKey(Cloth)
    text = models.TextField()

    class Meta():
        verbose_name = u'Комментарий'
        verbose_name_plural = u'Комментарии'

class Cart(models.Model):
    user = models.ForeignKey(User)
    items = models.ManyToManyField(Cloth, through='Proxy')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    addres = models.TextField()
    phone = models.CharField(max_length=40)
    comments = models.TextField()
    total = models.IntegerField(default=0)

    class Meta():
        verbose_name = u'Заказ'
        verbose_name_plural = u'Заказы'

class Contacts(models.Model):
    user = models.ForeignKey(User)
    addres = models.TextField()
    phone = models.CharField(max_length=40)

    class Meta():
        verbose_name = u'Контактные данные'
        ordering = ('user', )


class Proxy(models.Model):
    item = models.ForeignKey(Cloth)
    cart = models.ForeignKey(Cart)
    count = models.IntegerField()
    size = models.ForeignKey(Size)

    class Meta():
        verbose_name = u'Proxy'
        ordering = ('item', )