from django.db import models
from django.db.models import Model

class Customer(models.Model):
        Customer_id = models.IntegerField(primary_key=True)      
        username = models.CharField(max_length=50)       
        password = models.CharField(max_length=50)
        city = models.CharField(max_length=30)
        class Meta:
            db_table = "Customer"
class Account(models.Model):
        account_id = models.IntegerField(primary_key=True)
        Customerid = models.OneToOneField(Customer,on_delete=models.CASCADE)
        balance = models.BigIntegerField()
        createddate = models.DateField()
        deleteddate = models.DateField()
        class Meta:
            db_table = "Acoount"
class Transaction(models.Model):
        Transaction_id = models.IntegerField(primary_key=True)
        Transaction_type = models.CharField(max_length=50)
        Origin_id= models.ForeignKey(Customer, on_delete=models.CASCADE)
        Destination_id = models.IntegerField()       
        date = models.DateField()
        amount = models.IntegerField()
        done = models.BooleanField(default=False)
        class Meta:
            db_table = "Transaction"
            