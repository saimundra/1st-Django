from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def contactus(request):
    template = loader.get_template("contactus.html")
    return HttpResponse(template.render())
def thankyou(request):
    template = loader.get_template("thankyou.html")
    return HttpResponse(template.render())