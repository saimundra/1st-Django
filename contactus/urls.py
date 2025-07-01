from django.urls import path
from . import views

urlpatterns = [
    path("", views.contactus, name="contactus"),
    path('thankyou/', views.thankyou, name="thankyou")
]