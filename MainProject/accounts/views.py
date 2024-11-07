from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# Create your views here.
from django.views import View
from django.contrib import messages
def register(request):
    if request.method == 'GET':
        print(' GET method')
        context = {
        'page_name' : 'Register'
        }
        return render(request,'accounts/register.html',context)

    elif request.method == 'POST':
        
        print(' POST request')
        username = request.POST.get('Username')
        password = request.POST.get('password')
        user = User.objects.create_superuser(username=username,password=password)
        print(user)
        return redirect('/') 
from .forms import *
class Register(View):
    
    def get(self,request):
        print(' GET method')
        context = {
        'page_name' : 'Register',
        'user_form': UserRegisterForm(),
        'customer_form': CustomerRegisterForm(),
        }
        return render(request,'accounts/register.html',context)

    def post(self,request):
        user_form = UserRegisterForm(data=request.POST)
        customer_form = CustomerRegisterForm(data=request.POST,files=request.FILES)
        context = {
                'page_name' : 'Register',
                'user_form': user_form,
                'customer_form': customer_form,
                }
        if user_form.is_valid() and customer_form.is_valid():
            user = user_form.save(commit=False)
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            if password==confirm_password:
                user.password = password
            else:
                messages.error(request,'Password and Confirm password are not same')
                messages.info(request,'make sure password and confirm password should be same')
                return render(request,'accounts/register.html',context)
            user.save()
            customer = customer_form.save(commit=False)  
            customer.dob = request.POST.get('dob')
            customer.user = user
            customer.save()
        else:            
            messages.error(request,'Fill the Form correctly')
            return render(request,'accounts/register.html',context)
        return redirect('/')




def login(request):
    context = {
        'page_name' : 'Log In'
    }
    return render(request,'accounts/login.html',context)