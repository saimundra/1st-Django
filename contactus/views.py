from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def contactus(requests):
    return HttpResponse("<h1> THIS IS A CONTACT PAGE </h1>")