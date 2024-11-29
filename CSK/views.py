from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Rutraj(request):
    return HttpResponse('<h1><marquee>captain of csk</h1></marquee>')