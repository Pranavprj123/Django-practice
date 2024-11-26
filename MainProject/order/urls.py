from django.urls import path
from . import views

urlpatterns = [
    path('checkout/',views.Checkout.as_view(),name='checkout'),
    path('proceed-to-pay/',views.proceed_to_pay,name='proceed_to_pay'),
]