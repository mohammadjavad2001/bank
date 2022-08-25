from django.shortcuts import render
from site1.forms import *
from django.http import HttpResponse

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

