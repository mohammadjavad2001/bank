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


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
       model = Transaction
       fields = ('Transaction_id', 'Transaction_type', 'Origin_id', 'Destination_id','date','amount','done')



class joinSerializer(serializers.Serializer):
    Customer_id = serializers.CharField(max_length=200)
    age = serializers.IntegerField()
    username = serializers.DateTimeField()
    password = serializers.IntegerField()
    city = serializers.CharField(max_length=200)
    Transaction_id = serializers.IntegerField()
    Transaction_type = serializers.CharField(max_length=200)
    Origin_id = serializers.IntegerField()
    Destination_id = serializers.IntegerField()        
    Transaction_id = serializers.IntegerField()
    date = serializers.DateTimeField()
    amount = serializers.IntegerField()
    done = serializers.BooleanField()           