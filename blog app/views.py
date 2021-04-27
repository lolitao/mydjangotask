from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. which data is presented to user

def index(request):
    return HttpResponse("Have a nice day")
