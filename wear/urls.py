from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'store.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^detail/(?P<cloth_id>\d+)/$', 'wear.views.wear_detail'),
    url(r'^add_to_cart/(?P<cloth_id>\d+)/$', 'wear.views.cart_add'),
    url(r'^cart/$', 'wear.views.cart_view'),
    url(r'^category/(?P<cat>\d+)/$', 'wear.views.wear_list_cat'),
    url(r'^$', 'wear.views.wear_list'),
)
