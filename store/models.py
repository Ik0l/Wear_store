# -*- coding: utf-8 -*-

import re

from django.db import models
from django.db.models.query import QuerySet
from django.utils.translation import ugettext_lazy as _


class PublishQuerySet(QuerySet):

    def published(self, **kwargs):
        return self.filter(is_published=True, **kwargs)


class PublishManager(models.Manager):
    use_for_related_fields = True

    def get_query_set(self):
        return PublishQuerySet(self.model)

    def published(self, *args, **kwargs):
        return self.get_query_set().published(*args, **kwargs)


class PublishModel(models.Model):
    is_published = models.BooleanField(
        verbose_name=_(u'публикация'),
        help_text=_(u'Отображать/Скрыть'),
        default=True,
        db_index=True,
    )

    objects = PublishManager()

    @models.permalink
    def get_absolute_url(self):
        try:
            url_name = self.url_name
        except AttributeError:
            s = self.__module__
            r = r'(.+)\.models$'
            app = re.findall(r, s)[0].lower().replace('.', '_')
            cls = self.__class__.__name__.lower()
            url_name = '%s:%s_detail' % (app, cls, )
        return (url_name, [str(self.id)])

    class Meta:
        abstract = True
