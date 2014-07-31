'''
Created on Jul 30, 2014

@author: leon
'''
from django.conf.urls import patterns,url
from django.contrib.auth.views import login, logout

urlpatterns = patterns('auth.views',
    url(r'^login/$', login),
    url(r'^logout/$', logout),
)