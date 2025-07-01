from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.hashers import check_password
from signup.models import signup
# Create your views here.
def login(request):
    template = render(request, "login.html")
    return HttpResponse(template)

from django.contrib.auth.hashers import check_password

def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            user = signup.objects.get(email=email)
            print(user)
            if check_password(password, user.password):
                # ✅ Password matched - manually handle session here
                request.session['user_id'] = user.id
                return redirect('/aboutus/')
            else:
                return render(request, 'login.html', {'error': 'Invalid credentials'})
        except signup.DoesNotExist:
            return render(request, 'login.html', {'error': 'User not found'})
