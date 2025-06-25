from django.urls import path
from . import views

urlpatterns = [
    path("",views.HomePage, name ="HomePage"),
    path('thankyou/', views.thankyou, name="Thank you "),
    path("aboutus/", views.aboutus, name = "aboutus"),
    path("login/",views.login, name= "login")
]