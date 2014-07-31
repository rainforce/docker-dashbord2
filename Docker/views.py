'''
Created on Jul 31, 2014

@author: leon
'''

# from django.shortcuts import render_to_response
from django.template.response import TemplateResponse
from django.http import HttpResponse
import docker
import json

def list_base(request, reload_func):

    return TemplateResponse(request, 'list_base.html',{'reload_func':reload_func})


def search_registry(request):
    term = request.GET['term']
    cli = docker.Client(base_url='http://192.168.1.136:8765')
    result = cli.search(term)
    return HttpResponse(json.dumps(result))