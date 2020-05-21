from django.urls import path
from . import views



urlpatterns = [
    path('',  views.home, name= "home"),
    path('appointment.html',  views.appointment, name= "appointment"),
    path('lab.html',  views.lab, name= "lab"),
    path('contact.html',  views.contact, name= "contact"),
    path('doctor.html',  views.doctor, name= "doctor"),
    path('blog.html',  views.blog, name= "blog"),

 
]




