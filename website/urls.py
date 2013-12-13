from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'website.views.home'),
    url(r'^blog/$', 'website.views.blog'),
    url(r'^blog/(?P<slug>[\w-]+)/$', 'website.views.slug'),
    url(r'^blog/(?P<year>\d{4})/$', 'website.views.year'),
    url(r'^blog/(?P<year>\d{4})/(?P<month>\d{2})/)$', 'website.views.month'),
    url(r'^blog/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', 'website.views.day'),
)
