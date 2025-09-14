from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def my_art(request):
    return HttpResponse("Hello, this my art!")
