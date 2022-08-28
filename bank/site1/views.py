from ast import Try
from gzip import READ
import json
from django.shortcuts import render
from site1.forms import signupform
from django.http import HttpResponse
from django.http import response
from .models import *
from .serializers import CustomerSerializer     
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['GET'])
def home(request,age1):
#   def get_queryset():
#        c_age = request.query_params.get('age',False)
#        if c_age:
#            customers = Customer.objects.filter(age=c_age)
#        else:
#            customers = Customer.objects.all()
#        return customers   

#   customers1=get_queryset()   
   try:
      p=Customer.objects.get(age=age1)
   except p.DoesNotExist:
      return Response({'niiiist '})
   Customer_serial=CustomerSerializer(p)

   return Response(Customer_serial.data)
@api_view(['GET'])
def city(request,city1):
  
   try:
      p=Customer.objects.get(city=chr(city1))
   except p.DoesNotExist:
      return Response({'niiiist '})
   Customer_serial=CustomerSerializer(p)

   return Response(Customer_serial.data)   
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

