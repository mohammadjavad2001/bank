from django.db.models import Count
from ast import Delete
from collections import Counter
from datetime import date
from telnetlib import STATUS
from tempfile import tempdir
from django.db.models import F
from django.db.models import Avg
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import Http404
from django.core import serializers
from django.http import response

from .models import *
from site1.forms import signupform
from .serializers import AccountSerializer, CustomerSerializer, TransactionSerializer, joinSerializer     


from rest_framework import generics
from rest_framework import mixins
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

@api_view(['POST'])
#psoting with json in postman
def posttransaction(request):
   serialized_data=TransactionSerializer(data=request.data,many=True)
    
   if serialized_data.is_valid():

      obj = serialized_data.save()
      print("Fwwwwwwwwwwwwwwwwwwwwwwwwwww")
      print(type(obj))
      return Response(serialized_data.data,status=status.HTTP_200_OK)
   return Response(status=status.HTTP_400_BAD_REQUEST)     
@api_view(['GET'])
#psoting with json in postman
def gettransaction(request):
   query=Transaction.objects.all()
   serialized_data=TransactionSerializer(query,many=True)
   return Response(serialized_data.data,status=status.HTTP_200_OK)


@api_view(['GET'])
#http://127.0.0.1:8090/site1/home/?city=tehran
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
      #create new user 
      serialized_data=CustomerSerializer(data=request.data)
      
      if serialized_data.is_valid():

         obj = serialized_data.save()
         print("Fwwwwwwwwwwwwwwwwwwwwwwwwwww")
         print(type(obj))
         ad=obj.Customer_id
         temp = Account.objects.create(balance=0,createddate=date(2002, 12, 4).isoformat(),deleteddate=date(2008, 12, 4).isoformat(),account_id=Account.objects.all().count()+1,Customerid=Customer.objects.get(pk=obj.Customer_id))
         #temp.save()
        #entry_set.add(temp) # Associates Entry e with Blog b.
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
      Customer_found=Customer.objects.get(username=usenamesearch)
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

      customeredit.delete()
      return Response(status=status.HTTP_404_NOT_FOUND)
#api with Customerlistview
class CustomerListView(generics.GenericAPIView,
                        mixins.CreateModelMixin,
                        mixins.ListModelMixin):

   queryset = Customer.objects.all()
   serializer_class = CustomerSerializer
   def get(self,request,*args, **kwargs):
      return self.list(request,*args,**kwargs)



   def post(self,request,*args, **kwargs):
      return self.create(request,*args,**kwargs)      

class CustomerListdetails(generics.GenericAPIView,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.UpdateModelMixin):
                        #we must pass the pk in urls for this api
                        
   queryset = Customer.objects.all()
   serializer_class = CustomerSerializer         

   def get(self,request,*args,**kwargs):
      return self.retrieve(request,*args,**kwargs)

   def put(self,request,*args,**kwargs):
      return self.update(request,*args,**kwargs,partial=True)

   def delete(self,request,*args,**kwargs):
      return self.destroy(request,*args,**kwargs)   

      
            
#api by generic 
class CustomerGenericList(generics.ListCreateAPIView):
   queryset= Customer.objects.all()
   serializer_class = CustomerSerializer


class CustomerGenericfinder(generics.RetrieveUpdateDestroyAPIView):
   queryset= Customer.objects.all()
   serializer_class = CustomerSerializer

#psoting with json in postman

@api_view(['GET','POST'])
def avg_age_tehran(request):
   #query=list(Customer.objects.filter(Q(city='tehran'),Q(age__lt=35)))
   
   avg=Customer.objects.filter(Q(city='tehran')&Q(age__lt=35)).aggregate(Avg('age'))
   max=0
   counter=0
   #for i in Customer.objects.filter(Q(city='tehran'),Q(age__lt=35)):
   #   max+=i.age
   #   counter+=1
   #avg=max/counter      
   return Response(avg,status=status.HTTP_200_OK)
class join2(models.Model):
  def __init__(self, Customer_id, age, username,city ,password , Transaction_id,Transaction_type ,Origin_id , Destination_id,date,amount,done):
      self.Customer_id=Customer_id
      self.age=age
      self.username=username
      self.city=city
      self.password=password      
      self.Transaction_id=Transaction_id
      self.Transaction_type=Transaction_type
      self.Origin_id=Origin_id
      self.Destination_id=Destination_id
      self.date=date        
      self.amount=amount
      self.done=done   
@api_view(['GET','POST'])
def getrelated(request):
   #data78 = Customer.objects.select_related('Origin_id')#کارنمیکنه 
  
   data1 = Transaction.objects.all()
   queryset = Customer.objects.filter(Customer_id__in=data1.values('Origin_id'))                                                                                                                                                
   print(queryset)

   data=join2.objects.raw('SELECT * from "Customer" INNER JOIN "Transaction" on "Customer"."Customer_id"="Transaction"."Origin_id_id" where age>25') 
   serialized=joinSerializer(data,many=True)


   data5 = Customer.objects.all().annotate(Origin_id=F('Customer_id'))#serialized.data,   
   print(data5)
   Customer1 = Customer.objects.alias(entries=Counter('entry')).filter(entries__gt=5)
   
#   SomeModel_json = serializers.serialize("json", SomeModel.objects.all())
   return Response( serialized.data,status=status.HTTP_200_OK)

