from django.shortcuts import render

# Create your views here.
from django.template.response import TemplateResponse
import docker
import json

def list_images(request):
    cli = docker.Client(base_url='tcp://192.168.1.136:8765')
    data = cli.images()
    return TemplateResponse(request, 'list_images.html', {'images': data})