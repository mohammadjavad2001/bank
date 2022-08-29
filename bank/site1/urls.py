from django.contrib import admin  
from django.urls import path  
from site1 import views  
from . import views

urlpatterns = [
        path('signup/',views.signupform),
        path('home/',views.home),
        path('age/<int:age>/',views.ageget),
        path('wf/',views.wf),

]