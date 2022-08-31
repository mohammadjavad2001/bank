from rest_framework import serializers

from .models import *

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
       model = Account
       fields = ('account_id', 'balance', 'createddate','deleteddate','Customerid')
                   
class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
       model = Customer
       fields = ('Customer_id', 'username', 'password', 'age','city')




