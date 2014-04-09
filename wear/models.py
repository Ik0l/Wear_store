from django.db import models
from django.contrib.auth.models import User
# Create your models here. blank=True, null=True

class Category(models.Model):
    title = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % (self.title, )


class Cloth(models.Model):
    class Meta():
        db_table = 'cloth'
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

    def __unicode__(self):
        return u'%s' % (self.title)


class Size(models.Model):
    title = models.CharField(max_length=10)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return u'%s(%s)' % (self.title, self.category.title)


class SizeCount(models.Model):
    size = models.ForeignKey(Size)
    item = models.ForeignKey(Cloth)
    count = models.IntegerField(default=0)


class Gallery(models.Model):
    item = models.ForeignKey(Cloth)
    image = models.ImageField(upload_to="wear/galery", blank=True)


class Comments(models.Model):
    item = models.ForeignKey(Cloth)
    text = models.TextField()


class Cart(models.Model):
    user = models.ForeignKey(User)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    region = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=50)
    home = models.CharField(max_length=10)
    apart = models.CharField(max_length=5, blank=True)
    phone = models.CharField(max_length=30)
    comments = models.CharField(max_length=300)
    total = models.IntegerField(default=0)


class Contacts(models.Model):
    user = models.ForeignKey(User)
    region = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=50)
    home = models.CharField(max_length=10)
    apart = models.CharField(max_length=5, blank=True)
    phone = models.CharField(max_length=30)