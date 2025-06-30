from django.shortcuts import render,redirect
from django.contrib.auth import authenticate ,login
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def login(request):
    template = loader.get_template("login.html")
    return HttpResponse(template.render())

def login_view(request):
    email = request.POST['email']
    password = request.POST['password']
    
    user = authenticate(request,email = email, password= password)

    if user is not None:
        login(request,email)
        return(redirect('aboutus/'))
    else:
        return render(request, 'login.html',{'error':'invalid credentials'})

    return render(request, 'login.html') 

