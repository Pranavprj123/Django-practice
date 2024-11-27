from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import Payment,User,Order
from cart.models import Cart
import razorpay
# Create your views here.

@csrf_exempt
def confirm_payment(request):
    if request.method != 'POST':
        return redirect('/')
    else:
        try:
            RAZORPAY_KEY_ID = settings.RAZORPAY_KEY_ID
            RAZORPAY_KEY_SECRET = settings.RAZORPAY_KEY_SECRET
            
            client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))
            verify = {
                
                        'razorpay_order_id': request.POST.get('razorpay_order_id'),
                        'razorpay_payment_id': request.POST.get('razorpay_payment_id'),
                        'razorpay_signature': request.POST.get('razorpay_signature')
                        
            }
            print(verify)
            client.utility.verify_payment_signature({
                        'razorpay_order_id': request.POST.get('razorpay_order_id'),
                        'razorpay_payment_id': request.POST.get('razorpay_payment_id'),
                        'razorpay_signature': request.POST.get('razorpay_signature')

            })
            payment = get_object_or_404(Payment,razorpay_order_id = verify['razorpay_order_id'])
            payment.razorpay_payment_id = verify['razorpay_payment_id']
            payment.payment_signature = verify['razorpay_signature']
            payment.status = 'COMPLETED'
            payment.save()
            user = get_object_or_404(User,username = payment.user.username)
            order = get_object_or_404(Order,order_uuid = payment.order.order_uuid)
            Cart.objects.filter(user = user).delete()
            order.status = 'PENDING'
            order.save()

            return redirect('product_list')
            
        except Exception as e:
            print(e)
            return redirect('checkout/')