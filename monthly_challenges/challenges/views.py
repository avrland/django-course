from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

def index(request):
    return HttpResponse("This works!!")

def index2(request):
    return HttpResponse("Dupa!!")

def challenge(request, month):
    if month == "dupa":
        output = "DUPAAAAAAA"
    else:
        return HttpResponseNotFound("dssss")
    return HttpResponse(output)