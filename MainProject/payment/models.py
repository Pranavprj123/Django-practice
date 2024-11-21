from django.db import models
from django.contrib.auth.models import User
from order.models import Order
# Create your models here.

STATUS_CHOICE=[
        ('PENDING','PENDING'),
        ('COMPLETED','COMPLETED'),
        ('FAILED','FAILED')
]
METHOD_CHOICE = [
        ('RAZORPAY','RAZORPAY'),
        ('COD','COD'),
        ('KARMA_WALLET','KARMA_WALLET')
]
class Payment(models.Model):
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    razorpay_order_id = models.CharField(max_length=25,blank=True,default="default")
    razorpay_payment_id = models.CharField(max_length=25,blank=True,default="default")
    payment_signature=models.CharField(max_length=128,default='default',blank=True)
    amount=models.DecimalField(decimal_places=2,max_digits=12) 
    status=models.CharField(choices=STATUS_CHOICE,max_length=25)
    method=models.CharField(choices=METHOD_CHOICE,max_length=25)
    order=models.ForeignKey(Order,on_delete=models.DO_NOTHING)