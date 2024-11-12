from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def checkout(request):
    context = {

    }
    return render(request,'order/checkout.html',context)
