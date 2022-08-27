from rest_framework import viewsets

from . import models
from . import serializers


class CustomerViewset(viewsets.ModelViewSet):   
   queryset = models.Customer.objects.all()
   serializer_class = serializers.CustomerSerializer


class AccountViewset(viewsets.ModelViewSet):
   queryset = models.Account.objects.all()
   serializer_class = serializers.AccountSerializer
   
    