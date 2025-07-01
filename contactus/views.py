from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import contactus as ContactUs  # Rename to avoid naming conflict

# Create your views here.
def contactus(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            
            if name and email and message:
                new_contact = ContactUs(name=name, email=email, message=message)
                new_contact.save()
                return redirect('thankyou')
            else:
                return render(request, 'contactus.html', {'error': 'All fields are required'})
        except Exception as e:
            return render(request, 'contactus.html', {'error': str(e)})
    return render(request, 'contactus.html')

def thankyou(request):
    return render(request, 'thankyou.html')
        