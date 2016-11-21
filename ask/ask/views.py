#from django.shortcuts import render
#from django.http import HttpResponse 
#
#def test(request, *args, **kwargs):
#return HttpResponse('OK')

from django.http import HttpResponse, HttpResponseNotFound

def ktotam(request):
    return HttpResponse("Found!")

def nicogodomanet(request):
return HttpResponseNotFound("Not Found!")
