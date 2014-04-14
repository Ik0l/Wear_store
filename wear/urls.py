# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('wear.views',
    url(r'^$', 'wear_list_cat', {'cat_id': 0}, name='list_all'),
    url(r'^category/(?P<cat_id>\d+)/$', 'wear_list_cat', name='list_cat'),
    url(r'^detail/(?P<cloth_id>\d+)/$', 'wear_detail'),
    url(r'^add_comment/(?P<cloth_id>\d+)/$', 'add_comment'),
    url(r'^add_to_cart/(?P<cloth_id>\d+)/$', 'cart_add', name='add_to_cart'),
)
