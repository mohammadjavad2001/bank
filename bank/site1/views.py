from django.shortcuts import render
from site1.forms import signupform
from django.http import HttpResponse
from django.http import response
      
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['GET'])
def home(request):  
    return Response('HEllllllllllo')
def signup(request):
   username = "not logged in"
   
   if request.method == "POST":
      #Get the posted form
      MysignupForm = signup(request.POST)
      
      if MysignupForm.is_valid():
         username = MyLoginForm.cleaned_data['username']
   else:
      MysignupForm = signup()
		
   return render(request, 'loggedin.html', {"username" : username})

