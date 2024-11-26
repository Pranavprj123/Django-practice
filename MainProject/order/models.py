from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from accounts.models import Address
from uuid import uuid4
# Create your models here.
STATUSCHOICE=[
    ('CREATED','CREATED'),
    ('PENDING','PENDING'),
    ('DISPACHED','DISPACHED'),
    ('PROCESSING','PROCESSING'),
    ('OUT FOR DELIVERY','OUT FOR DELIVERY'),
    ('DELIVERED','DELIVERED'),
    ('CANCELED','CANCELED') ]

class Order(models.Model):
    order_uuid = models.UUIDField(primary_key=True,max_length=128,auto_created=True,default=uuid4())
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=20,choices=STATUSCHOICE,default='PENDING')
    order_on = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    total = models.DecimalField(max_digits=12,decimal_places=2)
    shipping_address = models.ForeignKey(Address,on_delete=models.CASCADE,blank=True) 
    shipping_charges = models.DecimalField(decimal_places=2,max_digits=10)
    # def save(self,using,commit = False,force_insert = False):
    #     self.order_uuid = uuid4() 
    #     super().save(force_insert=force_insert,using=using)
    #     if not commit:
    #         return self  

class OrderDetails(models.Model):
    order_id = models.ForeignKey(Order,on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=12,decimal_places=2)
