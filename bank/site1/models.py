from django.db import models
from django.db.models import Model

class Customer(models.Model):
        Customer_id = models.IntegerField(primary_key=True)
        age = models.IntegerField()      
        username = models.CharField(max_length=50)       
        password = models.CharField(max_length=50)
        city = models.CharField(max_length=30)
        class Meta:
            db_table = "Customer"
        def __str__(self):
            return self.username
                    
class Account(models.Model):
        account_id = models.IntegerField(primary_key=True)
        Customerid = models.OneToOneField(Customer,on_delete=models.CASCADE,related_name="accounts")
        balance = models.BigIntegerField()
        createddate = models.DateField()
        deleteddate = models.DateField()
        class Meta:
            db_table = "Acoount"
    
        def __str__(self):
            return str(self.account_id)
                    
class Transaction(models.Model):
        Transaction_id = models.IntegerField(primary_key=True)
        Transaction_type = models.CharField(max_length=50)
        Origin_id= models.ForeignKey(Customer, on_delete=models.CASCADE,related_name="originid")
        Destination_id = models.IntegerField()       
        date = models.DateField()
        amount = models.IntegerField()
        done = models.BooleanField(default=False)
        class Meta:
            db_table = "Transaction"
        def __str__(self):
            return self.Transaction_id
            
            