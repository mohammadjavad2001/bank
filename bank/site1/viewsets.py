from rest_framework import viewsets

from . import models
from . import serializers
from rest_framework import permissions


class CustomerViewset(viewsets.ModelViewSet):   
   #ModelViewSet az hame function ha ro dare val masalan ReadOnlyModelViewSet faghat retrieve ro dare 
   queryset = models.Customer.objects.all()
   serializer_class = serializers.CustomerSerializer
   permission_classes=[permissions.IsAuthenticated]


class AccountViewset(viewsets.ModelViewSet):
   queryset = models.Account.objects.all()
   serializer_class = serializers.AccountSerializer
   
    