from django.http import HttpResponse, HttpResponseNotFound

def ktotam(request):
    return HttpResponse("Found!")

def nicogodomanet(request):
return HttpResponseNotFound("Not Found!")
