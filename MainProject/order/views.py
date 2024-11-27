from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from accounts.models import Address
from django.conf import settings
from accounts.models import User,Customer,Address
from cart.models import Cart
from order.models import Order,OrderDetails
import razorpay
from payment.models import Payment
# @login_required(login_url='/accounts/login/')
class Checkout(View):
    # @login_required
    def get(self,request):
        address = Address.objects.filter(user = request.user)
        context={
            'address' : address
        }
        return render(request,'order/checkout.html',context)
    # @login_required
    def post(self,request):
        address_id= request.POST.get('address')
        if address_id:
            request.session['address_id'] = address_id
            return redirect('proceed_to_pay')
        else:
            return redirect('ceckout')
        
        
def proceed_to_pay(request):
    RAZORPAY_KEY_ID = settings.RAZORPAY_KEY_ID
    RAZORPAY_KEY_SECRET = settings.RAZORPAY_KEY_SECRET
    client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))
    user = User.objects.get(username = request.user)
    cart_item = Cart.objects.filter(user = request.user)
    total = 0
    order = Order.objects.filter(user = user).filter(status='CREATED').first()
    if not order:
        order = Order.objects.create(
            user = user,
            status = 'CREATED',
            total  = total,
            shipping_address = Address.objects.get(id=int(request.session['address_id'])),
            shipping_charges = 100
        )
    
    for item in cart_item:
        total += item.product.price_inclusive * item.quantity
        OrderDetails.objects.create(
            order_id = order,
            product = item.product,
            quantity = item.quantity,
            price = item.product.price_inclusive )
    order.total = total
    order.save()
    data = { "amount": int(total)*100, "currency": "INR", "receipt": str(order.order_uuid) }
    razor_pay_order = client.order.create(data=data)
    context = {
        'order':razor_pay_order,
        'data':data,
        'RAZORPAY_KEY_ID':RAZORPAY_KEY_ID,
    }
    Payment.objects.create(
        user = user,
        razorpay_order_id = razor_pay_order['id'],
        amount = total,
        status = 'PENDING',
        method = 'RAZORPAY',
        order = order
    )
    return render(request,'order/proceed_to_pay.html',context)