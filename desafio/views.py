from django.http import HttpResponse
from django.shortcuts import render
from .models import Familiar1
from .models import Familiar2
from .models import Familiar3

from django.template import loader
# Create your views here.

def una_vista(request):
    return HttpResponse('<h1>Proyecto</h1>')

def un_template(request):
    
    #template = loader.get_template('index.html')
    
    familiar1 = Familiar1(nombre='Lucas', phone= f'{123456}', fecha_nacimiento=15/2/1983)
    familiar2 = Familiar2(nombre='Julian', phone= f'{123456}', fecha_nacimiento=15/2/1983)
    familiar3 = Familiar3(nombre='Juana',  phone= f'{123456}', fecha_nacimiento=15/2/1983)
    familiar1.save()
    familiar2.save()
    familiar3.save()
    
    #render = template.render({'lista_objetos':[familiar1, familiar2, familiar3]})
    
    #return HttpResponse(render)
    
    
    return render(request, 'idex.html', {'lista_objetos':[familiar1, familiar2, familiar3]})