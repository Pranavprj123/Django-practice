from django.shortcuts import render

# Create your views here.
from .models import Brand
def brand_list(request):
    data = Brand.objects.all()
    context = {
        'brands' : data
    }
    return render(request,'product/brand_list.html',context)