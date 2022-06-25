from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def una_vista(request):
    return HttpResponse('<h1>Proyecto</h1>')

def un_template(request):
    
    template = loader.get_template('index.html')
    
    render = template.render({})
    
    return HttpResponse(render)