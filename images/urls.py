'''
Created on Jul 31, 2014

@author: leon
'''
from django.conf.urls import patterns,url
from Docker import views as common_views

urlpatterns = patterns('images.views',
    url(r'^$', common_views.list_base, {'reload_func':'images_reload'}),
    url(r'^all/$', 'list_images'),
)