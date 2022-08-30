from ast import Delete
from telnetlib import STATUS
from django.shortcuts import render
from site1.forms import signupform
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import Http404
from django.core import serializers
from django.http import response
from .models import *
from .serializers import CustomerSerializer     
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

def wf(request):
   mydata = Customer.objects.filter(Customer_id='18').values()
   print(mydata)
   mydata1 = CustomerSerializer(mydata)
   return Response(mydata1.data)
@api_view(['GET','POST'])
#psoting with json in postman
def postdata(request):
   city1 = request.data.get('city')
   cities=Customer.objects.filter(city=city1)
   Customer_serial=CustomerSerializer(cities,many=True)
   return Response(Customer_serial.data,status=status.HTTP_200_OK)


@api_view(['GET'])
def home(request):
#   def get_queryset():d
#        c_age = request.query_params.get('age',False)
#        if c_age:
#            customers = Customer.objects.filter(age=c_age)
#        else:
#            customers = Customer.objects.all()
#        retTurn customers   

#   customers1=get_queryset()  
   city1 = request.query_params.get('city')
   print(request.query_params)
   print(20*'=+')
   print(city1)
   try:
      
      cities=Customer.objects.filter(city=city1)
   except cities.DoesNotExist:
      return Response({'niiiist '})
   #qs_json = serializers.serialize('json', cities)
   #if many = true we can get a list of objects by serializer and convert to jason then print them
   Customer_serial=CustomerSerializer(cities,many=True)
   #Customer_serial.append(CustomerSerializer(cities[0]))
      # qs_json = serializers.serialize('json', qs)
   # Customer_serial=[]
   
   #print(type(Customer_serial[0]))
   #Customer_serial=CustomerSerializer(cities[0])
   #mydata = Customer.objects.filter(city='tehran').values()
   #return JsonResponse(cities, safe=False)
   return Response(Customer_serial.data,status=status.HTTP_200_OK)


@api_view(['GET'])
def ageget(request,age):

   #http://127.0.0.1:8090/site1/age/28/
   try:
      p=Customer.objects.get(age=age)
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
         username = MysignupForm.cleaned_data['username']
   if request.method == "GET":
      
      MysignupForm = signup()
		
   return render(request, 'loggedin.html', {"username" : username})

class CustomerList(APIView):
   def get(self,request):
      customers=Customer.objects.filter(age=37)
      serialized=CustomerSerializer(customers,many=True)
      return Response(serialized.data)
   def post(self,request):
      serialized_data=CustomerSerializer(data=request.data)
      if serialized_data.is_valid():
         serialized_data.save()
         return Response(serialized_data.data,status=status.HTTP_202_ACCEPTED)
      return Response(serialized_data.data,status=status.HTTP_400_BAD_REQUEST)     


class Customerfinder(APIView):
   def get_object(self,username1):
      try:
         customer=Customer.objects.get(username=username1)
      except Customer.DoesNotExist:
         raise Http404   
      return customer
   #get in url /site1/custonerfinder/amir/
   def get(self,request,usenamesearch):
      Customer_found=self.get_object(usenamesearch)
      serialized=CustomerSerializer(Customer_found)            
      return Response(serialized.data)  

   def put(self,request,usenamesearch):
      try:
         customeredit=Customer.objects.get(username=usenamesearch)
      except Customer.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND)
      serializer22=CustomerSerializer(customeredit,data=request.data,partial=True)
      #argument partial must be true then we can change only one field 
      if serializer22.is_valid():
         serializer22.save()
         return Response(serializer22.data)
      return Response(serializer22.data,status=status.HTTP_403_FORBIDDEN)         

   def delete(self,request,usenamesearch):
      try:
         customeredit=Customer.objects.get(username=usenamesearch)
      except Customer.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND)
      serializer22=CustomerSerializer(customeredit)

      serializer22.Delete()
      return Response(status=status.HTTP_204_NO_CONTENT)


