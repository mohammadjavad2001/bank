from django.shortcuts import render
from site1.forms import signupform
from django.http import HttpResponse
def signupform(request):  
    signing = signupform(request.POST)  
    return render(request,"signup.html",{'form':signing})  
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

