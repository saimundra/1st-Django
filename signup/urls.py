from django.urls import path
from . import views

urlpatterns = [
    path("/",views.signupForm, name = "signup")
   
]