from django import forms

from .models import *

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(max_length=30,widget=forms.PasswordInput(
        attrs={
        'placeholder':'Enter Password',
    }
    ))
    confirm_password = forms.CharField(max_length=30,widget=forms.PasswordInput(
        attrs={
        'placeholder':'Enter Password',
    }
    ))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
    
class CustomerRegisterForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.DateInput)
    class Meta:
        model = Customer
        exclude = ('user','dob')