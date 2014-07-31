from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Docker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^accounts/', include('accounts.urls')),
    url(r'^images/', include('images.urls')),
    url(r'^hosts/', include('hosts.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^registry/search/$', 'Docker.views.search_registry'),
)
