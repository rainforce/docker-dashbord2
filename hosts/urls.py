'''
Created on Jul 31, 2014

@author: leon
'''
from django.conf.urls import patterns,url
from Docker import views as common_views

urlpatterns = patterns('hosts.views',
    url(r'^$', common_views.list_base),
)