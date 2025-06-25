from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def HomePage(request):
    template = loader.get_template("homepage.html")
    return HttpResponse(template.render())

def thankyou(request):
    return HttpResponse("<h1> thank you for visting </h1>")

def aboutus(request):
    return HttpResponse("<h1> this is about us</h1>")

def login(request):
    return HttpResponse("<h1>enter your email and password to login</h1>")

