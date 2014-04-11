# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from store import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'store.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^detail/(?P<cloth_id>\d+)/$', 'wear.views.wear_detail'),
    url(r'^add_to_cart/(?P<cloth_id>\d+)/$', 'wear.views.cart_add'),
    url(r'^cart/$', 'wear.views.cart_view'),
    url(r'^category/(?P<cat_id>\d+)/$', 'wear.views.wear_list_cat'),
    url(r'^$', 'wear.views.wear_list'),
)

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns


    urlpatterns += static(
        settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT,
    )
    urlpatterns += staticfiles_urlpatterns()
