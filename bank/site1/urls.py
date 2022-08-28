from django.contrib import admin  
from django.urls import path  
from site1 import views  
from . import views

urlpatterns = [
        path('signup/',views.signupform),
        path('home/<int:age1>/',views.home),
        path('cityget/<str:city1>/',views.city),
]