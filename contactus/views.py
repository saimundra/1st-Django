from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from . models import contactus

# Create your views here.
def contactus(request):
    template = loader.get_template("contactus.html")
    return HttpResponse(template.render())
def thankyou(request):
    template = loader.get_template("thankyou.html")
    return HttpResponse(template.render())

def contact(request):
    if(request.method == 'POST'):
        print(request.POST)
        name = request. POST("name")
        email =request.POST("email") 
        message =request.Post("message")

        newdata = contactus(name = name , email = email, message = message)
        newdata.save()
        return redirect("/")
    elif(request.method == 'GET'):
        return render(request,"contactus.html")
        