from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import signup 
# Create your views here.

def signupForm(request):
    if(request.method == 'POST'):
        print(request.POST)
        first_name = request.POST['first_name']
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["password"]
        
        data = signup(first_name = first_name ,last_name = last_name, email = email, password = password, confirm_password = confirm_password)
        data.save()

        return redirect ('/')
    elif (request.method == 'GET'):
        return render(request, 'signup.html')