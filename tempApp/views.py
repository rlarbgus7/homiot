from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
from tempApp.models import Deshboard
from django.http import JsonResponse


# Create your views here.
def index(request):
    arti = loader.get_template('input.html').render()
    return HttpResponse(arti)

def input(request):
    arti = loader.get_template('index.html').render()
    return HttpResponse(arti)

def inputow(request):
    temp = request.GET['temp']
    hum = request.GET['hum']
    gas = request.GET['gas']

    temp = float(temp) if temp not in (None, '') else None
    hum = float(hum) if hum not in (None, '') else None
    gas = float(gas) if gas not in (None, '') else None

    print(temp)
    print(hum)
    print(gas)
    Deshboard.objects.create(temp=temp, hum=hum, gas=gas)
    return redirect('/input/')

def inpujson(request):
    data = list(Deshboard.objects.values())

    return JsonResponse(data, safe=False)

def test(request):
    data = Deshboard.objects.order_by('-seq')

    arti = loader.get_template('test.html').render(context={ 'data': data }, request=request)
    
    return HttpResponse(arti)