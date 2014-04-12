# -*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin

from store import settings


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'wear.views.index'),
    url(r'^wear/', include('wear.urls')),
    url(r'^cart/$', 'wear.views.cart_view'),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns


    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
    urlpatterns += staticfiles_urlpatterns()
