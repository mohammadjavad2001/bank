from django.contrib import admin  
from django.urls import path  
from site1 import views  
from . import views

urlpatterns = [
        path('signup/',views.signupform),
        path('home/',views.home),
        path('age/<int:age>/',views.ageget),
        path('wf/',views.wf),
        path('postdata/',views.postdata),
        path('customerlist/',views.CustomerList.as_view()),
        path('customerfinder/<str:usenamesearch>/',views.Customerfinder.as_view()),

        #we can define when GET:get POST:post        path('customerlist/',views.CustomerList.as_view({GET:get POST:post})),

        
]