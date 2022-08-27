from rest_framework import serializers

from .models import *


class CustomerSerializer(serializers.ModelSerializer):
   class Meta:
       model = Customer
       fields = ('Customer_id', 'username', 'age', 'password','city')


class AccountSerializer(serializers.ModelSerializer):
   class Meta:
       model = Account
       fields = ('Customerid', 'balance', 'createddate','deleteddate','account_id')
